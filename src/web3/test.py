from web3 import Web3 


w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/f0e34d2fdcaf4efea2eedc4afc7734c6'))

print('connected: ', w3.isConnected())

latest_block = w3.eth.get_block('latest')
print(latest_block)
