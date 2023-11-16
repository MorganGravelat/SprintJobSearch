import sys
import os

# Function to calculate the checksum
def calculate_checksum(text, checksum_size):
    checksum = 0
    original_length = len(text)
    padding_needed = 0  # Initialize padding_needed to 0

    # Determine the padding character for checksums other than 8-bit
    pad_char = 'X' if checksum_size in [16, 32] else ''

    # Check if padding is needed for 16-bit checksum
    if checksum_size == 16 and original_length % 2 != 0:
        text += pad_char
        padding_needed = 1

    # Check if padding is needed for 32-bit checksum
    elif checksum_size == 32:
        padding_needed = (4 - (original_length % 4)) % 4
        text += pad_char * padding_needed

    # Calculate checksum based on checksum size
    if checksum_size == 8:
        for char in text:
            checksum = (checksum + ord(char)) & 0xFF
    elif checksum_size == 16:
        for i in range(0, len(text), 2):
            word = (ord(text[i]) << 8) + ord(text[i+1])
            checksum = (checksum + word) & 0xFFFF
    elif checksum_size == 32:
        for i in range(0, len(text), 4):
            dword = (ord(text[i]) << 24) + (ord(text[i+1]) << 16) + (ord(text[i+2]) << 8) + ord(text[i+3])
            checksum = (checksum + dword) & 0xFFFFFFFF

    return checksum, original_length, padding_needed

# Function to split text into chunks of a specified size
def split_into_chunks(text, chunk_size=80):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

# Main program
if __name__ == "__main__":
    # Check if the correct number of command line arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_file> <checksum_size>")
        sys.exit(1)

    input_file_name = sys.argv[1]
    checksum_size = int(sys.argv[2])

    # Validate the checksum size
    if checksum_size not in [8, 16, 32]:
        sys.stderr.write("Valid checksum sizes are 8, 16, or 32\n")
        sys.exit(1)

    # Search for the input file in the current directory and its subdirectories
    found = False

    for root, _, files in os.walk('.'):
        for file in files:
            if file == input_file_name:
                input_file_path = os.path.join(root, file)

                # Open and read the input file
                with open(input_file_path, 'r') as file:
                    input_text = file.read()

                # Calculate the checksum and get the text length after padding
                checksum, original_text_length, padding_needed = calculate_checksum(input_text, checksum_size)

                # Echo the input text and any additional padding for 16-bit and 32-bit checksums
                echo_text = input_text
                if padding_needed > 0:
                    echo_text += 'X' * padding_needed

                for chunk in split_into_chunks(echo_text):
                    print(chunk)

                # Output the checksum in the specified format
                print(f"{checksum_size:2d} bit checksum is {checksum:8x} for all {original_text_length + padding_needed:4d} chars")

                found = True
                break  # Exit the loop after processing the file

    if not found:
        print(f"File '{input_file_name}' not found in the current directory and its subdirectories.")
