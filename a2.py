# Wikender Alcius
# CIS5730
# Assignment 1: Merkle Tree
# Phase 2: Verifying Integrity with Interim Hash

# verify_merkle_tree should output an error message if the interim hash does not exist in the tree. 
# for info, please output this as well: 
# print(f'Interim hash found at combination of {transactions[i]} and {transactions[i + 1]}')  

import hashlib

def sha256(data):
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

def verify_merkle_tree(transactions, expected_interim_hash):
    if not transactions:
        return

    current_level = transactions[:]
    
    # Store intermediate hashes
    while len(current_level) > 1:
        next_level = []
        if len(current_level) % 2 != 0:
            current_level.append(current_level[-1])

        for i in range(0, len(current_level), 2):
            combined = current_level[i] + current_level[i + 1]
            hashed = sha256(combined)
            if hashed == expected_interim_hash:
                print(f"Interim hash found at combination of transactions {i} and {i + 1}")
                print(f"Transactions: {current_level[i]}, {current_level[i + 1]}")
                return
            next_level.append(hashed)

        current_level = next_level

    print("Interim hash not found in Merkle tree.")

def read_transactions_from_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def main():
    transactions = read_transactions_from_file('a1.txt')
    # Replace this with any given interim hash to check
    expected_interim_hash = "36a17b6bc6311e408829353cbff4f0d9582231a23ef05ab08302bc9215005390"
    verify_merkle_tree(transactions, expected_interim_hash)

if __name__ == "__main__":
    main()
