from transaction import Transaction
from digital_signature import sign

class Wallet:
    def __init__(self, private_key, public_key):
        self.private_key = private_key
        self.public_key = public_key

    def create_transaction(self, receiver, amount):
        document = f"{self.public_key}:{receiver}:{amount}"
        print("Creating transaction:", document)
        signature = sign(self.private_key, document)
        return Transaction(self.public_key, receiver, amount, signature)

