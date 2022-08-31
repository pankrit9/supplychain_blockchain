"""
https://www.youtube.com/watch?v=pZSegEXtgAE
https://web3py.readthedocs.io/en/stable/examples.html
https://cryptomarketpool.com/how-to-listen-for-ethereum-events-using-web3-in-python/
"""

#==============================================================================#

import json
from web3 import Web3
import time
import urllib.request
import asyncio
from solcx import compile_source
from setting import URL_GUI, URL_GANACHE, LAND_CONTRACT_PATH, REGISTER_ORACLE_CONTRACT_PATH

#==============================================================================#

def compile_source_file(file_path):
   with open(file_path, 'r') as f:
      source = f.read()
   return compile_source(source)


def deploy_contract(web3, contract_interface):
    land_sol = web3.eth.contract(
        abi=contract_interface['abi'],
        bytecode=contract_interface['bin']
    )

    tx_hash = land_sol.constructor().transact()
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

    contract = web3.eth.contract(
        address=tx_receipt.contractAddress,
        abi=contract_interface['abi']
    )
    return tx_receipt.contractAddress, contract


def compile_and_deploy(filepath):
    web3 = Web3(Web3.HTTPProvider(URL_GANACHE))
    web3.eth.defaultAccount = web3.eth.accounts[0]

    # Compilation
    compiled_sol = compile_source_file(filepath)
    contract_id, contract_interface = compiled_sol.popitem()
    print(contract_id)
    # print(contract_interface)

    # Deployment
    address, contract = deploy_contract(web3, contract_interface)
    return (web3, address, contract)

#==============================================================================#

def handle_event(event):
    print("==============================================")
    print("[Event]")
    payload = json.loads(Web3.toJSON(event))["args"]
    print("land_hash:", payload["land_hash"])
    print("land_owner:",payload["land_owner"])
    print()
    url_path = f"{URL_GUI}/lands/{payload['land_hash']}/land_info.json"
    print(f"Fetching data from: {url_path}")

    try:
        url = urllib.request.urlopen(url_path)
    except Exception as e:
        print(e)
        return

    data = json.loads(url.read().decode())
    print(data)
    print("Attempting to register on lands.sol.")

    if data["owner_addr"] != payload["land_owner"]:
        print("Not the right owner. Cancel register.")
        return

    try: 
        location = f"{data['street_num']} {data['street']} {data['suburb']} {data['state']}"
        contract_land.functions.land_register(
            land_hash=data['land_hash'],
            location=location,
            owner_addr=payload["land_owner"],
        ).transact()
    except Exception as e:
        print(e)
        return
    print("Registered successfully.")


async def log_loop(event_filter, poll_interval):
    print("Listening for events... ")
    while True:
        for PairCreated in event_filter.get_new_entries():
            handle_event(PairCreated)
        await asyncio.sleep(poll_interval)

#==============================================================================#

def run_blockchain_listener():
    event_filter = contract_reg.events.request_land_event.createFilter(
        fromBlock="latest"
    )

    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(
            asyncio.gather(
                log_loop(
                    event_filter=event_filter,
                    poll_interval=2,
                )
            )
        )
    finally:
        loop.close()


if __name__ == '__main__':
    # Deploy land.sol
    (web3_land, address_land, contract_land) = compile_and_deploy(LAND_CONTRACT_PATH)
    print(f"[Main] Land Address:\n{address_land}\n")

    # Deploy register_oracle.sol
    (web3_reg, address_reg, contract_reg) = compile_and_deploy(REGISTER_ORACLE_CONTRACT_PATH)
    print(f"[Main] Register Oracle Address:\n{address_reg}\n")

    # Register default account as the contract owner for land.sol
    web3_land.eth.defaultAccount = web3_land.eth.accounts[0]
    web3_reg.eth.defaultAccount = web3_land.eth.accounts[0]
    print(f"[Main] Default account:\n{web3_land.eth.defaultAccount}\n")
    print("\n")

    run_blockchain_listener()
