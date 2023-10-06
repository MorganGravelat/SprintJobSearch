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
