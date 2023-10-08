'''In this assignment you’ll write a program that encrypts the alphabetic letters in a file using the
Hill cipher where the Hill matrix can be any size from 2x2 up to 9x9. Your program will take
two command line parameters containing the names of the file storing the encryption key and
the file to be encrypted. The program must generate output to the console (terminal) screen as
specified below.'''

import sys
import numpy as np
import string
import math
import re

    '''=============================================================================
    |  Function encrypt
    |  Purpose:  Encrypts the message using the key
    |  Parameters:  message: String to be encrypted
    |               key: 2D array of ints
    |  Returns:  encrypted message
    +============================================================================='''
def encrypt(message, key):
    #Convert message to uppercase
    message = message.upper()
    #Remove all non-alphabetic characters
    message = re.sub(r'[^A-Za-z]', '', message)
    #Convert message to numbers
    message = [ord(c) - ord('A') for c in message]
    #Convert message to 2D array
    message = np.array(message)
    message = np.reshape(message, (-1, len(key)))
    #Multiply message by key
    message = np.dot(message, key)
    #Modulo 26
    message = np.mod(message, 26)
    #Convert message to string
    message = ''.join([chr(c + ord('A')) for c in np.reshape(message, (-1))])
    return message

    '''=============================================================================
    |  Function decrypt
    |  Purpose:  Decrypts the message using the key
    |  Parameters:  message: String to be decrypted
    |               key: 2D array of ints
    |  Returns:  decrypted message
    +============================================================================='''
def decrypt(message, key):
    #Convert message to uppercase
    message = message.upper()
    #Remove all non-alphabetic characters
    message = re.sub(r'[^A-Za-z]', '', message)
    #Convert message to numbers
    message = [ord(c) - ord('A') for c in message]
    #Convert message to 2D array
    message = np.array(message)
    message = np.reshape(message, (-1, len(key)))
    #Find inverse of key
    key = np.linalg.inv(key)
    #Multiply message by key
    message = np.dot(message, key)
    #Modulo 26
    message = np.mod(message, 26)
    #Convert message to string
    message = ''.join([chr(c + ord('A')) for c in np.reshape(message, (-1))])
    return message

    '''=============================================================================
    |  Function getKey
    |  Purpose:  Reads the key from the file
    |  Parameters:  keyFile: String containing the name of the file with the key
    |  Returns:  key: 2D array of ints
    +============================================================================='''
def getKey(keyFile):
    #Read key from file
    key = np.loadtxt(keyFile, dtype=int)
    return key

    '''=============================================================================
    |  Function getMessage
    |  Purpose:  Reads the message from the file
    |  Parameters:  messageFile: String containing the name of the file with the message
    |  Returns:  message: String containing the message
    +============================================================================='''
def getMessage(messageFile):
    #Read message from file
    message = open(messageFile, 'r').read()
    return message

    '''=============================================================================
    |  Function main
    |  Purpose:  Main function
    |  Parameters:  None
    |  Returns:  None
    +============================================================================='''
def main():
    #Read command line arguments
    keyFile = sys.argv[1]
    messageFile = sys.argv[2]
    #Get key and message
    key = getKey(keyFile)
    message = getMessage(messageFile)
    #Encrypt and decrypt message
    encryptedMessage = encrypt(message, key)
    decryptedMessage = decrypt(encryptedMessage, key)
    #Print results
    print('Key matrix:')
    print(key)
    print('Message:')
    print(message)
    print('Encrypted message:')
    print(encryptedMessage)
    print('Decrypted message:')
    print(decryptedMessage)
###################################
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

# This function reads through the matrix filename called file_name and returns an array of arrays of each row of the matrix read from the file
def key_matrix_array(file_name):
    file = open(file_name, 'r') #open opens a file and returns it as a file object 'r' stands for the mode read
    n = int(file.readline()) #reads the first line of the key matrix file and converts it to an integer
    key_matrix = []
    for _ in range(n): #The key matrix has n rows specified at the top and n is iterating through the number of rows
        row = list(map(int, file.readline().split())) #Each time you call readline() it reads the next line of the file so all you need is n  to iterate the number of times the matrix specifies
        # the map function runs the same function on each piece of data created by split and turns them into ints shoving them into a row array
        key_matrix.append(row) #appends the row to the key matrix array
    file.close() #this method closes the file
    return key_matrix #returns the key matrix array

# this function goes throug the provided plaintext file and turns it into a string of all lowercase letters
def read_plaintext(filename):
    with open(filename, 'r') as file:
        plaintext = file.read()
    # Remove characters that are not alphabetic and not part of the English alphabet
    cleaned_text = ''.join(char.lower() for char in plaintext if char.isalpha() and ((ord('a') <= ord(char) <= ord('z')) or (ord('A') <= ord(char) <= ord('Z'))))
    return cleaned_text

# This function complies with the instructions and pads the plaintext with x's to make it comply with key size
def pad_plaintext(plaintext, key_size):
    # takes the key size which is the number of rows in the key matrix and subtracts the length of the plaintext
    padding_length = key_size - (len(plaintext) % key_size)
    if padding_length > 0:
        plaintext += 'x' * padding_length
    return plaintext

def encrypt(key_matrix, plaintext):
    key_size = len(key_matrix)
    ciphertext = ""
    for i in range(0, len(plaintext), key_size):
        block = plaintext[i:i+key_size]
        encrypted_block = []
        for row in key_matrix:
            result = 0
            for k, char in enumerate(block):
                result += row[k] * (ord(char) - ord('a'))
            encrypted_block.append(result % 26 + ord('a'))
        ciphertext += ''.join([chr(char) for char in encrypted_block])
    return ciphertext

# Function that finds file by name in the currrent folder or subfolders
def file_search(file_name):
    for root_path, _, files in os.walk("."): #os.walk is going to essentially walk me through the file structure starting at the current file directory and going down
        if file_name in files: # Checking if the file is in the current folder and searching down to the subfolders
            return os.path.join(root_path, file_name)  #Will combine various path components with the propert directory seperator /
    return None # None is returned upon a file not being inside the current file structure or sub structures

def main():
    if len(sys.argv) != 3:
        sys.exit(1)

    key_filename = sys.argv[1]
    plaintext_filename = sys.argv[2]

    key_filepath = file_search(key_filename)
    plaintext_filepath = file_search(plaintext_filename)

    key_matrix = key_matrix_array(key_filepath)
    plaintext = read_plaintext(plaintext_filepath)
    plaintext = pad_plaintext(plaintext, len(key_matrix))
    ciphertext = encrypt(key_matrix, plaintext)

    print("Key matrix:")
    for row in key_matrix:
        print("   " + "   ".join(map(str, row)))

    print("\nPlaintext:")
    for i in range(0, len(plaintext), 80):
        print(plaintext[i:i+80])

    print("\nCiphertext:")
    chunk_size = 80
    for i in range(0, len(ciphertext), chunk_size):
        print(ciphertext[i:i+chunk_size])


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
