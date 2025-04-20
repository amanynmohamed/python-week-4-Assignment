# This program reads from 'input.txt', makes all text uppercase, and writes it to 'modified_output.txt'

try:
    # Open and read content from 'input.txt'
    with open('output.txt', 'r') as file:
        content = file.read()

    # Convert content to uppercase
    modified_content = content.upper()

    # Write the modified content to 'modified_output.txt'
    with open('modified_output.txt', 'w') as new_file:
        new_file.write(modified_content)

    print("Done! File has been read and modified successfully.")

except FileNotFoundError:
    print("Error: 'input.txt' file not found.")
except IOError:
    print("Error: Could not read or write the file.")
    





