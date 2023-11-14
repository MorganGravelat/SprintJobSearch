"""=============================================================================
| Assignment: pa02 - Calculating an 8, 16, or 32 bit
| checksum on an ASCII input file
|
| Author: Morgan Gravelat
| Language: Python
|
| To Compile: python pa02.py //Caution - expecting input parameters
|
|
| To Execute: python-> python3 pa02.py inputFile.txt 8
|
| where inputFile.txt is an ASCII input file
| and the number 8 could also be 16 or 32
| which are the valid checksum sizes, all
| other values are rejected with an error message
| and program termination
|
| Note: All input files are simple 8 bit ASCII input
|
| Class: CIS3360 - Security in Computing - Fall 2023
| Instructor: McAlpin
| Due Date: Nov 12 at 11:59pm
|
+============================================================================="""

import sys
import os

def calculate_checksum(text, checksum_bits):

    checksum = 0
    text_size = len(text)
    padding_count = 0


    if checksum_bits in [16, 32]:
        padding = 'X'
    else:
        padding = ''


    if checksum_bits == 16 and text_size % 2 != 0:
        text += padding
        padding_count = 1


    elif checksum_bits == 32:
        padding_count = (4 - (text_size % 4)) % 4
        text += padding * padding_count


    if checksum_bits == 8:
        for char in text:
            checksum = (checksum + ord(char)) & 0xFF
    elif checksum_bits == 16:
        for i in range(0, len(text), 2):
            chars = (ord(text[i]) << 8) + ord(text[i+1])
            checksum = (checksum + chars) & 0xFFFF
    elif checksum_bits == 32:
        for i in range(0, len(text), 4):
            chars = (ord(text[i]) << 24) + (ord(text[i+1]) << 16) + (ord(text[i+2]) << 8) + ord(text[i+3])
            checksum = (checksum + chars) & 0xFFFFFFFF


    return checksum, text_size, padding_count


def text_size_limiter(text, text_width=80):

    text_chunks = []
    for i in range(0, len(text), text_width):
        text_chunk = text[i:i+text_width]
        text_chunks.append(text_chunk)

    return text_chunks


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Please input in this format => python3 pa02.py <input_file> <checksum_bits(8/16/32)>")
        sys.exit(1)

    text_file_name = sys.argv[1]
    checksum_bits = int(sys.argv[2])

    if checksum_bits not in [8, 16, 32]:
        sys.stderr.write("Valid checksum sizes are 8, 16, or 32\n")
        sys.exit(1)

    file_found = False

    for root, _, files in os.walk('.'):
        for file in files:
            if file == text_file_name:
                input_file_path = os.path.join(root, file)

                with open(input_file_path, 'r') as file:
                    input_text = file.read()

                checksum, text_size, padding_count = calculate_checksum(input_text, checksum_bits)

                original_text = input_text
                if padding_count > 0:
                    original_text += 'X' * padding_count

                for text_chunk in text_size_limiter(original_text):
                    print(text_chunk)

                print(f"{checksum_bits:2d} bit checksum is {checksum:8x} for all {text_size + padding_count:4d} chars")

                file_found = True
                break

    # If file is not found, print message
    if not file_found:
        print(f"{text_file_name} not found")

"""=============================================================================
| I Morgan Gravelat (mo870937) affirm that this program is
| entirely my own work and that I have neither developed my code together with
| any another person, nor copied any code from any other person, nor permitted
| my code to be copied or otherwise used by any other person, nor have I
| copied, modified, or otherwise used programs created by others. I acknowledge
| that any violation of the above terms will be treated as academic dishonesty.
+============================================================================"""
