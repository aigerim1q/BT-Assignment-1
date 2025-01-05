from rsa import generate_keys
from wallet import Wallet
from blockchain import Blockchain
from database import save_transaction, load_transactions

public_key, private_key = generate_keys()
print("Public Key:", public_key)
print("Private Key:", private_key)

wallet = Wallet(private_key, public_key)


blockchain = Blockchain()

transaction = wallet.create_transaction("ReceiverPublicKey", 100)
print("Transaction created:", transaction.__dict__)
save_transaction(transaction)

transactions = load_transactions()
for tx in transactions:
    blockchain.add_transaction(tx, public_key)

blockchain.mine_block()

print("Blockchain mined:", [[tx.__dict__ for tx in block] for block in blockchain.chain])
