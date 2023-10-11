'''============================================================================
| Assignment: pa01 - Encrypting a plaintext file using the Hill cipher
|
| Author: Morgan Gravelat
| Language: python
|
| To Execute: python3 pa01.py kX.txt pX.txt
| where kX.txt is the keytext file
| and pX.txt is plaintext file
| Note:
| All input files are simple 8 bit ASCII input
| All execute commands above have been tested on Eustis
|
| Class: CIS3360 - Security in Computing - Fall 2023
| Instructor: McAlpin
| Due Date: October 8th, 2023
+==========================================================================='''

import sys
import os

def key_matrix_array(file_name):
    file = open(file_name, 'r')
    n = int(file.readline())
    key_matrix = []
    for _ in range(n):
        row = list(map(int, file.readline().split()))
        key_matrix.append(row)
    file.close()
    return key_matrix

def write_plaintext(filename):
    with open(filename, 'r') as file:
        plaintext = file.read()
    cleaned_text = ''.join(char.lower() for char in plaintext if char.isalpha() and ((ord('a') <= ord(char) <= ord('z')) or (ord('A') <= ord(char) <= ord('Z'))))
    return cleaned_text

def add_padding_plaintext(plaintext, key_size):
    padding_length = key_size - (len(plaintext) % key_size)
    if padding_length > 0:
        plaintext += 'x' * padding_length
    return plaintext

def hill_cipher(key_matrix, plaintext):
    key_size = len(key_matrix)
    ciphertext = ""
    for i in range(0, len(plaintext), key_size):
        block = plaintext[i:i+key_size]
        cipher_block = []
        for row in key_matrix:
            result = 0
            for k, char in enumerate(block):
                result += row[k] * (ord(char) - ord('a'))
            cipher_block.append(result % 26 + ord('a'))
        ciphertext += ''.join([chr(char) for char in cipher_block])
    return ciphertext

def file_search(file_name):
    for root_path, _, files in os.walk("."):
        if file_name in files:
            return os.path.join(root_path, file_name)
    return None

def main():
    if len(sys.argv) != 3:
        print("Proper Execution: python3 pa01.py kX.txt pX.txt")
        sys.exit(1)

    key_filename = sys.argv[1]
    plaintext_filename = sys.argv[2]

    key_filepath = file_search(key_filename)
    plaintext_filepath = file_search(plaintext_filename)

    if key_filepath is None and plaintext_filepath is None:
        print(f"{key_filename} and {plaintext_filename} are not found")
        sys.exit(1)
    if plaintext_filepath is None:
        print(f"{plaintext_filename} is not found")
        sys.exit(1)
    if key_filepath is None:
        print(f"{key_filename} is not found")
        sys.exit(1)

    key_matrix = key_matrix_array(key_filepath)
    plaintext = write_plaintext(plaintext_filepath)
    plaintext = add_padding_plaintext(plaintext, len(key_matrix))
    ciphertext = hill_cipher(key_matrix, plaintext)

    print("Key matrix:")
    for row in key_matrix:
        formatted_row = " "+" ".join(f"{num:3d}" for num in row)
        print(formatted_row)

    print("\nPlaintext:")
    for i in range(0, len(plaintext), 80):
        print(plaintext[i:i+80])

    print("\nCiphertext:")
    for i in range(0, len(ciphertext), 80):
        print(ciphertext[i:i+80])

if __name__ == "__main__":
    main()



'''=============================================================================
| I Morgan Gravelat (mo870937) affirm that this program is
| entirely my own work and that I have neither developed my code together with
| any another person, nor copied any code from any other person, nor permitted
| my code to be copied or otherwise used by any other person, nor have I
| copied, modified, or otherwise used programs created by others. I acknowledge
| that any violation of the above terms will be treated as academic dishonesty.
+============================================================================='''
