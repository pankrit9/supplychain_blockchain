#==============================================================================#

import os

#==============================================================================#

FILE_DIR = "__documents__"
FILE_PATH = f"{os.getcwd()}/{FILE_DIR}"

#==============================================================================#

PORT_GUI = 5000
PORT_GANACHE = 7545

URL_GUI = f'http://127.0.0.1:{PORT_GUI}'
URL_GANACHE = f'http://127.0.0.1:{PORT_GANACHE}'

LAND_CONTRACT_PATH = r'contracts/land.sol'
REGISTER_ORACLE_CONTRACT_PATH = r'contracts/register_oracle.sol'

#==============================================================================#
