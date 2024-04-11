import os
from web3 import Web3

infura_url = 'https://mainnet.infura.io/v3/{}'.format(os.getenv("INFURA_KEY"))
web3 = Web3(Web3.HTTPProvider(infura_url))
print(web3.isConnected())