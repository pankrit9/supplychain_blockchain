// Khiet Tam Nguyen - z5313514
// Ported from Week 04 Tutorial Handout
// 20.07.2021

import Web3 from "web3";
import { Contract, DeployOptions } from "web3-eth-contract";
const axios = require("axios").default;

(async () => {
    const web3Provider = new Web3.providers.WebsocketProvider("ws://localhost:7545");
    const web3 = new Web3(web3Provider);

    // Add an existing account
    let account = web3.eth.accounts.wallet.add("0x" + "81c8142ccbfc6a5098f34901b9f1e9ae9e40d7b5528a5fae938084013bc579aa");
    // console.log(account);

    // Compile
    const fs = require("fs");
    const solc = require("solc");
    function findImports(importPath: string) {
        try {
            return {
                contents: fs.readFileSync('smart_contracts/${importPath', "utf8")
            };
        } catch (e) {
            return {
                error: e.message
            }
        };
    }

    function compileSols(solNames: string[]): any {
        interface SolCollection { [key: string]: any };
        let sources: SolCollection = {};
        solNames.forEach((value: string, index: number, array: string[]) => {
            let sol_file = fs.readFileSync(`smart_contracts/${value}.sol`, "utf8");
            sources[value] = {
                content: sol_file
            };
        });
        let input = {
            language: "Solidity",
            sources: sources,
            settings: {
                outputSelection: {
                    "*": {
                        "*": ["*"]
                    }
                }
            }
        };
        let compiler_output = solc.compile(JSON.stringify(input), {
            import: findImports
        });
        let output = JSON.parse(compiler_output);
        return output;
    }

    let compiled = compileSols(["example"]);

    // console.log(compiled);
    // console.log(compiled.contracts.example.CoatIndicator);

    let contract_instance: Contract;
    let gasPrice: string;
    let contract = new web3.eth.Contract(compiled.contracts["example"]["CoatIndicator"].abi,
        undefined, {
        data: "0x" + compiled.contracts["example"]["CoatIndicator"].evm.bytecode.object
    });

    await web3.eth.getGasPrice().then((averageGasPrice) => {
        gasPrice = averageGasPrice;
    }).catch(console.error);


    await contract.deploy({
        data: contract.options.data,
        arguments: [account.address]
    } as DeployOptions).send({
        from: account.address,
        gasPrice: gasPrice!,
        gas: Math.ceil(1.2 * await contract.deploy({
            data: contract.options.data,
            arguments: [account.address]
        } as DeployOptions).estimateGas({
            from: account.address
        })),
    }).then((instance) => {
        contract_instance = instance;
    }).catch(console.error);

    // console.log(contract_instance!);
    console.log(contract_instance!.options.address);


    // Listen
    contract_instance!.events["temperatureRequest(string)"]()
    .on("connected", function (subscriptionId: any) {
        console.log("listening on event temperatureRequest");
    })
    .on("data", async function (event: any) {
        let city = event.returnValues.city;
        console.log(city);
        /// TODO respond with temperature by calling responsePhase(int256)

        let temperature = await axios.get(`https://goweather.herokuapp.com/weather/${city}`)
        .then(async function (response: any) {
            return response?.data?.temperature?.replace(/[^0-9-\.]/g, "");
        })
        .catch(function (error: any) {
            console.log(error);
        });
        if (!parseInt(temperature)) {
            console.log("invalid temperature");
            return;
        }
        console.log(temperature);

        try {
            contract_instance.methods["responsePhase(int256)"](temperature).send({
                from: account.address,
                gasPrice: gasPrice!,
                gas: Math.ceil(1.2 * await contract_instance.methods["responsePhase(int256)"]
                               (temperature).estimateGas({ from: account.address })),
            }).then(function (receipt: any) {
                return receipt;
            }).catch((err: any) => {
                console.error(err);
            });
        } catch (e) {
            console.log(e);
        }
    })
    .on("error", function (error: any, receipt: any) {
        console.log(error);
        console.log(receipt);
        console.log("error listening on event temperatureRequest");
    });
})();
