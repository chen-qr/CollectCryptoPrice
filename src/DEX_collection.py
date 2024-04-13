import os
from web3 import Web3
from uniswap_conofig import uniswap_router_address, uniswap_router_abi

infura_url = 'https://mainnet.infura.io/v3/{}'.format(os.getenv("INFURA_KEY"))
web3_client = Web3(Web3.HTTPProvider(infura_url))
assert web3_client.is_connected(), "Con not concect to infura!"

address = Web3.to_checksum_address(uniswap_router_address)
print(web3_client.eth.get_balance(address))

uniswap_contract = web3_client.eth.contract(address=address, abi=uniswap_router_abi)

slot0 = pool_contract.functions.slot0().call()
print(slot0)