from transaction import Transaction

def save_transaction(transaction, filename="transactions.txt"):
    with open(filename, "a") as file:
        serialized_data = f"{transaction.sender[0]},{transaction.sender[1]},{transaction.receiver},{transaction.amount}," \
                          f"{'|'.join(map(str, transaction.signature))}\n"
        file.write(serialized_data)
    print("Transaction saved to database.")

def load_transactions(filename="transactions.txt"):
    transactions = []
    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()  
                if not line:  
                    continue
                
                sender_part1, sender_part2, receiver, amount, signature = line.split(",", 4)
                sender = (int(sender_part1), int(sender_part2))  
                amount = int(amount) 
                signature = list(map(int, signature.split("|")))  
                
                transactions.append(Transaction(sender, receiver, amount, signature))
        print("Transactions loaded from database.")
    except FileNotFoundError:
        print("Database file not found. Starting fresh.")
    return transactions
