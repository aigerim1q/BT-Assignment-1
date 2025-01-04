from digital_signature import verify

class Transaction:
    def __init__(self, sender, receiver, amount, signature):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.signature = signature

def verify_transaction(transaction, public_key):
    document = f"{transaction.sender}:{transaction.receiver}:{transaction.amount}"
    print("Verifying transaction:", document)
    if not verify(public_key, document, transaction.signature):
        raise ValueError("Signature is wrong")
    print("Transaction is valid")
