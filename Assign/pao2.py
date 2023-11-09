import sys
import os

# Function to calculate the checksum
def calculate_checksum(text, checksum_size):
    # Initialize the checksum value based on the checksum size
    if checksum_size == 8:
        checksum = 0
    elif checksum_size == 16:
        checksum = 0
    elif checksum_size == 32:
        checksum = 0
    else:
        sys.stderr.write("Valid checksum sizes are 8, 16, or 32\n")
        sys.exit(1)

    for char in text:
        # Calculate the checksum here (e.g., update the running total)
        if checksum_size == 8:
            checksum = (checksum + ord(char)) & 0xFF
        elif checksum_size == 16:
            checksum = (checksum + ord(char)) & 0xFFFF
        elif checksum_size == 32:
            checksum = (checksum + ord(char)) & 0xFFFFFFFF

    return checksum

# Function to process a file and calculate checksum
def process_file(file_path, checksum_size):
    with open(file_path, 'r') as file:
        input_text = file.read()

    # Echo the input text with 80 characters per row (80 characters per line)
    for i in range(0, len(input_text), 80):
        print(input_text[i:i + 80])

    # Calculate the checksum
    checksum = calculate_checksum(input_text, checksum_size)

    # Pad the input text with 'X' characters to match the checksum size
    while len(input_text) % (checksum_size // 4) != 0:
        input_text += 'X'

    # Output the checksum
    print(f"{checksum_size} bit checksum is {checksum:0{checksum_size // 4}x} for all {len(input_text)} chars")

# Main program
if __name__ == "__main":
    # Check if the correct number of command line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python checksum.py <checksum_size>")
        sys.exit(1)

    checksum_size = int(sys.argv[1])

    # Validate the checksum size
    if checksum_size not in [8, 16, 32]:
        sys.stderr.write("Valid checksum sizes are 8, 16, or 32\n")
        sys.exit(1)

    # Search for files in the current directory and process them
    for root, _, files in os.walk('.'):
        for file in files:
            if file.endswith(".txt"):
                print(f"Processing file: {os.path.join(root, file)}")
                process_file(os.path.join(root, file), checksum_size)
