'''=============================================================================
| I Morgan Gravelat (mo870937) affirm that this program is
| entirely my own work and that I have neither developed my code together with
| any another person, nor copied any code from any other person, nor permitted
| my code to be copied or otherwise used by any other person, nor have I
| copied, modified, or otherwise used programs created by others. I acknowledge
| that any violation of the above terms will be treated as academic dishonesty.
+============================================================================='''
import sys

def copy_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as input_file:
            with open(output_filename, 'w') as output_file:
                for line in input_file:
                    output_file.write(line)
        print(f"File '{input_filename}' copied to '{output_filename}' successfully.")
    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python pa01.py <input_filename> <output_filename>")
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    copy_file(input_filename, output_filename)
