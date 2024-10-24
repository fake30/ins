import math

def encrypt(plaintext, key):
    """Encrypt plaintext using the columnar transposition cipher."""
    # Remove spaces and convert the plaintext to uppercase
    plaintext = plaintext.replace(" ", "").upper()

    # Calculate the number of columns required based on the key length
    num_columns = len(key)
    # Calculate the number of rows required
    num_rows = math.ceil(len(plaintext) / num_columns)

    # Create an empty grid to hold the transposed message
    grid = [['' for _ in range(num_columns)] for _ in range(num_rows)]

    # Fill in the grid with the plaintext characters
    idx = 0
    for col in range(num_columns):
        for row in range(num_rows):
            if idx < len(plaintext):
                grid[row][col] = plaintext[idx]
                idx += 1

    # Create the ciphertext by reading the columns according to the key order
    ciphertext = ""
    for col in key:
        col_idx = key.index(col)
        for row in range(num_rows):
            ciphertext += grid[row][col_idx]

    return ciphertext

def decrypt(ciphertext, key):
    """Decrypt ciphertext using the columnar transposition cipher."""
    # Calculate the number of columns required based on the key length
    num_columns = len(key)
    # Calculate the number of rows required
    num_rows = math.ceil(len(ciphertext) / num_columns)

    # Determine the number of characters in the last column
    extra_chars = (num_columns * num_rows) - len(ciphertext)

    # Create an empty grid to hold the transposed message
    grid = [['' for _ in range(num_columns)] for _ in range(num_rows)]

    # Calculate the number of full columns before the extra characters
    full_cols = num_columns - extra_chars

    # Populate the grid with the ciphertext characters
    idx = 0
    for col in range(num_columns):
        if col < full_cols:
            num_chars = num_rows
        else:
            num_chars = num_rows - 1
        for row in range(num_chars):
            grid[row][col] = ciphertext[idx]
            idx += 1

    # Read the grid to obtain the plaintext
    plaintext = ""
    for row in range(num_rows):
        for col in key:
            col_idx = key.index(col)
            plaintext += grid[row][col_idx]

    return plaintext

# Example usage
plaintext = "HELLO WORLD"
key = "KEY"
encrypted_text = encrypt(plaintext, key)
decrypted_text = decrypt(encrypted_text, key)

print("Plaintext:", plaintext)
print("Encrypted text:", encrypted_text)
print("Decrypted text:", decrypted_text)
