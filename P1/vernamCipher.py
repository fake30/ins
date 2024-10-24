import random

def generate_random_key(length):
    """Generate a random key of the specified length."""
    key = [random.randint(0, 255) for _ in range(length)]
    return bytes(key)

def vernam_encrypt(plaintext, key):
    """Encrypt plaintext using the Vernam cipher."""
    if len(plaintext) != len(key):
        raise ValueError("Plaintext and key must be of the same length")
    encrypted_text = bytearray()
    for i in range(len(plaintext)):
        encrypted_char = plaintext[i] ^ key[i]
        encrypted_text.append(encrypted_char)
    return bytes(encrypted_text)

def vernam_decrypt(encrypted_text, key):
    """Decrypt encrypted text using the Vernam cipher."""
    if len(encrypted_text) != len(key):
        raise ValueError("Encrypted text and key must be of the same length")
    decrypted_text = bytearray()
    for i in range(len(encrypted_text)):
        decrypted_char = encrypted_text[i] ^ key[i]
        decrypted_text.append(decrypted_char)
    return bytes(decrypted_text)

# Example usage
plaintext = "Hello, World!"
plaintext_bytes = plaintext.encode()  # Convert plaintext to bytes
key = generate_random_key(len(plaintext_bytes))
encrypted_text = vernam_encrypt(plaintext_bytes, key)
decrypted_text = vernam_decrypt(encrypted_text, key)

print("Plaintext:", plaintext)
print("Key:", key)
print("Encrypted text (hex):", encrypted_text.hex())  # Display encrypted text in hex format
print("Decrypted text:", decrypted_text.decode(errors='ignore'))  # Ignore errors during decoding
