import requests

# File containing Bitcoin addresses to check
address_file = "addresses.txt"

def get_balance(address):
    # Use the Blockchain.com API to get the balance of a given address
    url = f"https://blockchain.info/balance?active={address}"
    response = requests.get(url)
    try:
        data = response.json()
        return data[address]["final_balance"]
    except KeyError:
        print(f"Invalid address or KeyError: {address}")
        return None
    except:
        print(f"Unexpected error occured while processing address: {address}")
        return None

with open(address_file) as f:
    addresses = f.readlines()

# Remove newline characters from addresses
addresses = [address.strip() for address in addresses]

# Open the output file
with open("hits.txt", "w") as output_file:
    for address in addresses:
        balance = get_balance(address)
        if balance and float(balance) > 0:
            output_file.write(f"Address: {address} - Balance: {balance}\n")
        print(f"Address: {address} - Balance: {balance}")
