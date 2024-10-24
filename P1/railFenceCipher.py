def rail_fence_encrypt(plaintext, rails):
    """Encrypt the plaintext using the Rail Fence cipher."""
    # Create the rail fence pattern
    fence = [[' ' for _ in range(len(plaintext))] for _ in range(rails)]
    row, col, direction = 0, 0, 1  # direction 1 means moving downward, -1 means moving upward

    for char in plaintext:
        fence[row][col] = char
        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1
        row += direction
        col += 1

    # Read the encrypted message from the fence pattern
    encrypted_text = ''.join(char for row in fence for char in row if char != ' ')
    return encrypted_text

def rail_fence_decrypt(ciphertext, rails):
    """Decrypt the ciphertext using the Rail Fence cipher."""
    # Create the rail fence pattern with the same dimensions
    fence = [[' ' for _ in range(len(ciphertext))] for _ in range(rails)]

    # Mark the positions of the characters in the fence pattern
    row, col, direction = 0, 0, 1
    for _ in range(len(ciphertext)):
        fence[row][col] = '*'
        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1
        row += direction
        col += 1

    # Fill in the rail fence pattern with the characters from the ciphertext
    idx = 0
    for r in range(rails):
        for c in range(len(ciphertext)):
            if fence[r][c] == '*':
                fence[r][c] = ciphertext[idx]
                idx += 1

    # Read the decrypted message from the fence pattern
    decrypted_text = ''
    row, col, direction = 0, 0, 1
    for _ in range(len(ciphertext)):
        decrypted_text += fence[row][col]
        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1
        row += direction
        col += 1

    return decrypted_text

# Example usage
plaintext = "HELLO WORLD"
rails = 3
encrypted_text = rail_fence_encrypt(plaintext, rails)
decrypted_text = rail_fence_decrypt(encrypted_text, rails)

print("Plaintext:", plaintext)
print("Encrypted text:", encrypted_text)
print("Decrypted text:", decrypted_text)
