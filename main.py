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


if __name__ == "__main__":
    blockchain = Blockchain()

    for i in range(20):
        blockchain.add_transaction(f"User{i}", f"User{i+1}", i * 10)
        blockchain.add_transaction(f"User{i}", f"User{i+1}", i * 10)

    print("Майнинг первого блока...")
    blockchain.mine_block()

    blockchain.chain[0].hash = "0000"

    print("Майнинг второго блока...")
    blockchain.mine_block()

    blockchain.add_transaction("UserX", "UserY", -50)

    print("Целостность блокчейна:", blockchain.validate_blockchain())

    if len(blockchain.chain) > 1:
        blockchain.chain[1].transactions[0].amount = 9999

    for block in blockchain.chain:
        print(f"Блок {block.index} | Хэш: {block.hash} | Предыдущий хэш: {block.previous_hash}")
