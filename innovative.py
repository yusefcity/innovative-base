```python
from web3 import Web3
import json

# Connect to Base network
rpc_url = "https://mainnet.base.org"
w3 = Web3(Web3.HTTPProvider(rpc_url))

private_key = "YOUR_PRIVATE_KEY"
account = w3.eth.account.from_key(private_key)

contract_address = Web3.to_checksum_address(
    "0x1234567890123456789012345678901234567890"
)

# jamejam project metadata
project_name = "jamejam"
network_name = "base"
project_idea = "idea"

nonce = w3.eth.get_transaction_count(account.address)

transaction = {
    "to": contract_address,
    "value": 0,
    "gas": 120000,
    "gasPrice": w3.eth.gas_price,
    "nonce": nonce,
    "chainId": 8453,
    "data": "0x"
}

signed_transaction = w3.eth.account.sign_transaction(
    transaction,
    private_key
)

transaction_info = {
    "project": project_name,
    "network": network_name,
    "idea": project_idea,
    "from": account.address,
    "to": contract_address,
    "nonce": nonce,
    "hash": signed_transaction.hash.hex()
}

print("Contract interaction signed successfully")
print(json.dumps(transaction_info, indent=2))

# Optional broadcast
# tx_hash = w3.eth.send_raw_transaction(
#     signed_transaction.raw_transaction
# )
# print(tx_hash.hex())

# Thank you
```
