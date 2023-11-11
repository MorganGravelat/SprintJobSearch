import sys
import os

# Function to calculate the checksum
def calculate_checksum(text, checksum_size):
    checksum = 0

    if checksum_size == 8:
        pad_char = '\n'
    else:
        pad_char = 'X'

    # Pad the input text with the appropriate character to match the checksum size
    while len(text) % (checksum_size // 8) != 0:
        text += pad_char

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

    return checksum, len(text)



# Main program
if __name__ == "__main__":
    # Check if the correct number of command line arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python pa02.py <input_file> <checksum_size>")
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

                # Echo the input text
                print(input_text)

                # Calculate the checksum
                checksum, text_length = calculate_checksum(input_text, checksum_size)

                # Output the checksum in the specified format
                print(f"{checksum_size} bit checksum is {checksum:0{checksum_size // 4}x} for all {text_length} chars")

                found = True
                break  # Exit the loop after processing the file

    if not found:
        print(f"File '{input_file_name}' not found in the current directory and its subdirectories.")
