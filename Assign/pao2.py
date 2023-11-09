import sys

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

# Main program
if __name__ == "__main__":
    # Check if the correct number of command line arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python checksum.py <input_file> <checksum_size>")
        sys.exit(1)

    input_file = sys.argv[1]
    checksum_size = int(sys.argv[2])

    # Validate the checksum size
    if checksum_size not in [8, 16, 32]:
        sys.stderr.write("Valid checksum sizes are 8, 16, or 32\n")
        sys.exit(1)

    # Open and read the input file
    with open(input_file, 'r') as file:
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
