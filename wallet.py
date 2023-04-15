import sys
import requests
from web3 import Web3
from datetime import datetime

INFURA_API_KEY = "YOUR_INFURA_API_KEY"
ETHERSCAN_API_KEY = "YOUR_ETHERSCAN_API_KEY"  # Uzupełnij swoim kluczem API Etherscan


def main():
    w3 = Web3(Web3.HTTPProvider(f"https://mainnet.infura.io/v3/{INFURA_API_KEY}"))

    if not w3.is_connected():
        print("Nie udało się połączyć z siecią Ethereum.")
        sys.exit(1)

    eth_address = input("Wprowadź adres portfela MetaMask Ethereum: ")

    if not w3.is_address(eth_address):
        print("Nieprawidłowy adres Ethereum.")
        sys.exit(1)

    address = w3.to_checksum_address(eth_address)
    balance = w3.from_wei(w3.eth.get_balance(address), 'ether')
    print(f"Saldo konta {eth_address}: {balance} ETH")

    transactions = get_last_transactions(address, 5)

    if transactions:
        print("5 ostatnich transakcji:")
        for i, tx in enumerate(transactions, start=1):
            print(f"{i}.")
            print(f"  Hash: {tx['hash']}")
            print(f"  Od: {tx['from']}")
            print(f"  Do: {tx['to']}")
            print(f"  Wartość: {int(tx['value']) / 10 ** 18} ETH")
            print(f"  Opłata: {int(tx['gasPrice']) * int(tx['gasUsed']) / 10 ** 18} ETH")
            print(f"  Data: {datetime.utcfromtimestamp(int(tx['timeStamp']))}")
            print(f"  Blok: {tx['blockNumber']}")
            print()
    else:
        print("Nie udało się pobrać transakcji.")


def get_last_transactions(eth_address, n=5):
    url = f"https://api.etherscan.io/api?module=account&action=txlist&address={eth_address}&sort=desc&apikey={ETHERSCAN_API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data["status"] == "1":
            transactions = data["result"][:n]
            return transactions
    return None


if __name__ == "__main__":
    main()
