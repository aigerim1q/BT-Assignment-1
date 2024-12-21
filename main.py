import hashlib

def hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

class MerkleTree:
    def __init__(self, transactions):
        self.transactions = transactions
        self.root = self.compute_merkle_root(transactions)

    def compute_merkle_root(self, transactions):
        if len(transactions) == 1:
            return hash(transactions[0])

        current_level = [hash(tx) for tx in transactions]
        while len(current_level) > 1:
            new_level = []
            for i in range(0, len(current_level), 2):
                left = current_level[i]
                right = current_level[i + 1] if i + 1 < len(current_level) else left
                new_level.append(hash(left + right))
            current_level = new_level
        return current_level[0]

