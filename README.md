# ETH Balance Tracker
The application is a Python script that retrieves the balance and last 5 transactions of an Ethereum wallet address using Infura and Etherscan APIs.

This Python script uses Infura and Etherscan APIs to retrieve the balance and the last 5 transactions of an Ethereum wallet address. It imports the sys, requests, Web3, and datetime modules and defines an INFURA_API_KEY and an ETHERSCAN_API_KEY.

The main() function initializes a Web3 object, prompts the user for an Ethereum wallet address, retrieves the balance and prints it, and calls the get_last_transactions() function to retrieve and print the last 5 transactions.

The get_last_transactions() function takes an Ethereum address and an optional number of transactions to retrieve, sends a GET request to an Etherscan API URL, and returns the specified number of transactions if the response is successful.

To run the script, the user needs to replace the API key placeholders with their own keys and execute the script in a terminal or command prompt using python wallet.py.

![image](https://user-images.githubusercontent.com/96372115/232220545-90cda8ae-2d14-46cc-a6d8-680e38ac9aaa.png)
