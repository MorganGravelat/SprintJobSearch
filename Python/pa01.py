'''=============================================================================
| I Morgan Gravelat (mo870937) affirm that this program is
| entirely my own work and that I have neither developed my code together with
| any another person, nor copied any code from any other person, nor permitted
| my code to be copied or otherwise used by any other person, nor have I
| copied, modified, or otherwise used programs created by others. I acknowledge
| that any violation of the above terms will be treated as academic dishonesty.
+============================================================================='''

import sys
import os

def find_file(filename):
    # Search for the file in the current directory and its subdirectories
    for root, _, files in os.walk("."):
        if filename in files:
            return os.path.join(root, filename)
    return None

def read_key_matrix(filename):
    with open(filename, 'r') as file:
        n = int(file.readline())
        key_matrix = []
        for _ in range(n):
            row = list(map(int, file.readline().split()))
            key_matrix.append(row)
    return key_matrix

def read_plaintext(filename):
    with open(filename, 'r') as file:
        plaintext = file.read()
    # Clean the plaintext by removing non-alphabetic characters and converting to lowercase
    plaintext = ''.join(char.lower() for char in plaintext if char.isalpha())
    return plaintext

def pad_plaintext(plaintext, key_size):
    padding_length = key_size - (len(plaintext) % key_size)
    if padding_length > 0:
        plaintext += 'x' * padding_length
    return plaintext

def encrypt(key_matrix, plaintext):
    key_size = len(key_matrix)
    ciphertext = ""
    for i in range(0, len(plaintext), key_size):
        block = plaintext[i:i+key_size]
        encrypted_block = [0] * key_size
        for j in range(key_size):
            for k in range(key_size):
                encrypted_block[j] += key_matrix[j][k] * (ord(block[k]) - ord('a'))
            encrypted_block[j] %= 26
            encrypted_block[j] += ord('a')
        ciphertext += ''.join([chr(char) for char in encrypted_block])
    return ciphertext

def main():
    if len(sys.argv) != 3: # sys.argv is the variable of the number of arguments given by the command call. Less than 3 will cause my program to exit using sys.exit with a 1 error code.
        print("What to enter -> python3 pa01.py <key_filename> <text_filename> Make sure there are exactly 3 arguments or the program will exit") #This is asking the
        sys.exit(1)

    key_filename = sys.argv[1]
    plaintext_filename = sys.argv[2]

    # Try to find the key file and plaintext file in the current directory and subdirectories
    key_filepath = find_file(key_filename)
    plaintext_filepath = find_file(plaintext_filename)

    if key_filepath is None:
        print(f"Key file '{key_filename}' not found.")
        sys.exit(1)

    if plaintext_filepath is None:
        print(f"Plaintext file '{plaintext_filename}' not found.")
        sys.exit(1)

    key_matrix = read_key_matrix(key_filepath)
    plaintext = read_plaintext(plaintext_filepath)
    plaintext = pad_plaintext(plaintext, len(key_matrix))
    ciphertext = encrypt(key_matrix, plaintext)

    print("Key matrix:")
    for row in key_matrix:
        print(" ".join(map(str, row)))

    print("\nPlaintext:")
    # Print the plaintext in lines of 80 characters or less
    for i in range(0, len(plaintext), 80):
        print(plaintext[i:i+80])

    print("\nCiphertext:")
    chunk_size = 80
    for i in range(0, len(ciphertext), chunk_size):
        print(ciphertext[i:i+chunk_size])

if __name__ == "__main__":
    main()
