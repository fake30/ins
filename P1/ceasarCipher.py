def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            # Determine whether the character is uppercase or lowercase
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')
            # Apply the Caesar cipher shift
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted_text += shifted_char
        else:
            # If the character is not a letter, keep it as is
            encrypted_text += char
    return encrypted_text

# Example usage
plaintext = "Hello, World!"
shift = 3
encrypted_text = caesar_cipher(plaintext, shift)
print("Encrypted text:", encrypted_text)
