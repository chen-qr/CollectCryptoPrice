import os
from web3 import Web3
import json

infura_url = 'https://mainnet.infura.io/v3/{}'.format(os.getenv("INFURA_KEY"))
web3_client = Web3(Web3.HTTPProvider(infura_url))
assert web3_client.is_connected(), "Con not concect to infura!"

uniswap_v3_config = json.load(open("config/contracts/uniswap_v3.json"))
factory_v2_config = json.load(open("config/contracts/factory_v2.json"))

address = Web3.to_checksum_address(uniswap_v3_config.address)
assert web3_client.eth.get_balance(address) >= 0, "Balance is not enough!"

uniswap_contract = web3_client.eth.contract(address=address, abi=uniswap_v3_config.ABI)

factoryV2Address = uniswap_contract.functions.factoryV2().call()
assert factoryV2Address == factory_v2_config.address, "factoryV2Address is not correct!"
