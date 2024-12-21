import hashlib
import time

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
class Block:
    def init(self, index, previous_hash, transactions):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = time.time()
        self.transactions = transactions  
        self.merkle_root = MerkleTree(transactions).root 
        self.hash = self.compute_hash()
def compute_hash(self):
        """
        Вычисляет хэш блока на основе его данных.
        """
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.merkle_root}"
        return hash(block_string)

# Blockchain Class
class Blockchain:
    def init(self):
        self.chain = []
        self.pending_transactions = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, "0", ["Genesis Block"])
        self.chain.append(genesis_block)

    def add_transaction(self, sender, receiver, amount):
        transaction = f"{sender}->{receiver}:{amount}"
        self.pending_transactions.append(transaction)
