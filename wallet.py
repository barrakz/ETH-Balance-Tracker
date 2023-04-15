from web3 import Web3
from web3.middleware import geth_poa_middleware

w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/63bf9152e4dd497ea23ff239fa0fcec0"))

w3.middleware_onion.inject(geth_poa_middleware, layer=0)

address = input("Podaj adres konta MetaMask: ")

balance = w3.eth.get_balance(address)

print("Saldo portfela: {} ETH".format(Web3.from_wei(balance, "ether")))

