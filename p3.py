# Message Authentication Code

# Ensure the cryptography library is installed:
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import hmac
from cryptography.exceptions import InvalidSignature

# Generate a random secret key for HMAC
secret_key = b'SuperSecretKey'

# Message to be authenticated
message = b'Hello, HMAC!'

# Create an HMAC object
hmac_obj = hmac.HMAC(secret_key, hashes.SHA256())

# Update the HMAC object with the message
hmac_obj.update(message)

# Generate the HMAC (Message Authentication Code)
mac = hmac_obj.finalize()

print("Original Message:", message.decode())
print("HMAC:", mac.hex())

# Verify the HMAC

# Re-create the HMAC object with the same secret key
hmac_verify_obj = hmac.HMAC(secret_key, hashes.SHA256())

# Update the HMAC object with the received message
hmac_verify_obj.update(message)

try:
    # Verify the HMAC
    hmac_verify_obj.verify(mac)
    print("HMAC verification: Message is authentic and unchanged.")
except InvalidSignature:
    print("HMAC verification: Message has been tampered with or is not authentic.")
