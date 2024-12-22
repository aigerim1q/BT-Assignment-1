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
    def __init__(self, index, previous_hash, transactions):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = time.time()
        self.transactions = transactions
        self.merkle_root = MerkleTree(transactions).root
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.merkle_root}"
        return hash(block_string)

class Blockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, "0", ["Genesis Block"])
        self.chain.append(genesis_block)

    def add_transaction(self, sender, receiver, amount):
        transaction = f"{sender}->{receiver}:{amount}"
        self.pending_transactions.append(transaction)

    def mine_block(self):
        if len(self.pending_transactions) < 10:
            raise ValueError("Недостаточно транзакций для майнинга блока!")

        transactions = self.pending_transactions[:10]
        self.pending_transactions = self.pending_transactions[10:]

        last_block = self.chain[-1]
        new_block = Block(len(self.chain), last_block.hash, transactions)
        self.chain.append(new_block)

    def validate_blockchain(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.previous_hash != previous_block.hash:
                return False

            if current_block.hash != current_block.compute_hash():
                return False

        return True

if __name__ == "__main__":
    blockchain = Blockchain()

    for i in range(20):
        blockchain.add_transaction(f"User{i}", f"User{i+1}", i * 10)

    print("Майнинг первого блока...")
    blockchain.mine_block()
    print("Майнинг второго блока...")
    blockchain.mine_block()

    print("Целостность блокчейна:", blockchain.validate_blockchain())

    for block in blockchain.chain:
        print(f"Блок {block.index} | Хэш: {block.hash} | Предыдущий хэш: {block.previous_hash}")
