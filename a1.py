# Wikender Alcius
# CIS5730
# Assignment 1: Merkle Tree
# Phase 1: Building the Merkle Tree


import hashlib
import math

def read_transactions_from_file(file_path):
    # Implementation to read transactions from file
    try:
        with open(file_path, 'r') as file:
            transactions = [line.strip() for line in file] 
            return transactions
    except FileNotFoundError:
        return [] 

def sha256(data):
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

def build_merkle_tree(transactions):
    # Implementation to build the Merkle tree
    if not transactions:
        return None

    current_level = math.log(len(transactions), 2) - 1

    while len(transactions) > 1:

        if len(transactions) % 2 != 0:
            transactions.append(transactions[-1]) #duplicate the last transaction if odd

        next_level = []
        print("\n CURRENT LEVEL:", int(current_level))

        for i in range(0, len(transactions), 2):
            combined= transactions[i] + transactions[i + 1]
            hashed = sha256(combined)
            print(f"Computed hash = SHA256({transactions[i]} + {transactions[i + 1]})")
            next_level.append(hashed)


        transactions = next_level
        current_level -= 1

    return transactions[0]

def main():
    # Read the transactions from the file
    transactions = read_transactions_from_file('a1.txt')

    # Build the Merkle tree and get the top hash
    top_hash = build_merkle_tree(transactions)

    print(f"Top hash of the Merkle tree: {top_hash}")

    # Assert the top hash matches the expected hash
    assert top_hash == "2d800e7a04fa0e27ced3c37f9dc1086309304d2d6660bade4ecee773c06b1652", "Computed top hash does not match the expected top hash."


if __name__ == "__main__":
    main()
