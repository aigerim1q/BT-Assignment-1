from transaction import verify_transaction

class Blockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []

    def add_transaction(self, transaction, public_key):
        try:
            verify_transaction(transaction, public_key)
            self.pending_transactions.append(transaction)
        except ValueError as e:
            print(e)

    def mine_block(self):
        print("Mining block with transactions:", len(self.pending_transactions))
        self.chain.append(self.pending_transactions)
        self.pending_transactions = []

