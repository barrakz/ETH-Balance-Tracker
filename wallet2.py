import sys
import requests
from web3 import Web3
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

INFURA_API_KEY = "63bf9152e4dd497ea23ff239fa0fcec0"
ETHERSCAN_API_KEY = "HWTK4C8Z7G1U2MZPAGKB98J936BBR55DZ1"


def get_last_transactions(eth_address, n=5):
    url = f"https://api.etherscan.io/api?module=account&action=txlist&address={eth_address}&sort=desc&apikey={ETHERSCAN_API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data["status"] == "1":
            transactions = data["result"][:n]
            return transactions
    return None


def show_balance():
    eth_address = address_entry.get()
    w3 = Web3(Web3.HTTPProvider(f"https://mainnet.infura.io/v3/{INFURA_API_KEY}"))

    if not w3.is_connected():
        messagebox.showerror("Błąd", "Nie udało się połączyć z siecią Ethereum.")
        return

    if not w3.is_address(eth_address):
        messagebox.showerror("Błąd", "Nieprawidłowy adres Ethereum.")
        return

    address = w3.to_checksum_address(eth_address)
    balance = w3.from_wei(w3.eth.get_balance(address), 'ether')
    messagebox.showinfo("Informacja", f"Saldo konta {eth_address}: {balance} ETH")


def show_transactions():
    eth_address = address_entry.get()
    transactions = get_last_transactions(eth_address, 5)

    if transactions:
        transaction_info = "5 ostatnich transakcji:\n\n"
        for i, tx in enumerate(transactions, start=1):
            transaction_info += f"{i}.\n"
            transaction_info += f"  Hash: {tx['hash']}\n"
            transaction_info += f"  Od: {tx['from']}\n"
            transaction_info += f"  Do: {tx['to']}\n"
            transaction_info += f"  Wartość: {int(tx['value']) / 10 ** 18} ETH\n"
            transaction_info += f"  Opłata: {int(tx['gasPrice']) * int(tx['gasUsed']) / 10 ** 18} ETH\n"
            transaction_info += f"  Data: {datetime.utcfromtimestamp(int(tx['timeStamp']))}\n"
            transaction_info += f"  Blok: {tx['blockNumber']}\n\n"
        messagebox.showinfo("Informacja", transaction_info)
    else:
        messagebox.showerror("Błąd", "Nie udało się pobrać transakcji.")


# Tworzenie okna
window = tk.Tk()
window.title("Sprawdź saldo konta Ethereum")
window.geometry("400x300")

# Tworzenie etykiety i pola do wprowadzania adresu Ethereum
address_label = tk.Label(window, text="Adres Ethereum:")
address_label.pack(pady=10)
address_entry = tk.Entry(window)
address_entry.pack()

# Tworzenie przycisku do sprawdzenia salda
balance_button = tk.Button(window, text="Sprawdź saldo", command=show_balance)
balance_button.pack()

# Tworzenie przycisku do wyświetlenia ostatnich transakcji

transactions_button = tk.Button(window, text="Ostatnie transakcje", command=show_transactions)
transactions_button.pack()

window.mainloop()
