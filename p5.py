# secure key exchange using Diffie-Hellman (DH) parameters in Python,

# Ensure you have the cryptography library installed:
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization

# Generate Alice's private and public keys
alice_parameters = dh.generate_parameters(generator=2, key_size=2048)
alice_private_key = alice_parameters.generate_private_key()

# Serialize and save Alice's public parameters and public key to files
alice_parameters_pem = alice_parameters.parameter_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.ParameterFormat.PKCS3
)
alice_public_key_pem = alice_private_key.public_key().public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)
with open("alice_parameters.pem", "wb") as f:
    f.write(alice_parameters_pem)
with open("alice_public_key.pem", "wb") as f:
    f.write(alice_public_key_pem)

# Load Alice's public parameters and public key
with open("alice_parameters.pem", "rb") as f:
    alice_parameters_pem = f.read()
alice_parameters = serialization.load_pem_parameters(alice_parameters_pem)

with open("alice_public_key.pem", "rb") as f:
    alice_public_key_pem = f.read()
alice_public_key = serialization.load_pem_public_key(alice_public_key_pem)

# Generate Bob's private and public keys
bob_parameters = alice_parameters  # Bob uses Alice's parameters
bob_private_key = bob_parameters.generate_private_key()

# Serialize and save Bob's public key to a file
bob_public_key_pem = bob_private_key.public_key().public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)
with open("bob_public_key.pem", "wb") as f:
    f.write(bob_public_key_pem)

# Load Bob's public key
with open("bob_public_key.pem", "rb") as f:
    bob_public_key_pem = f.read()
bob_public_key = serialization.load_pem_public_key(bob_public_key_pem)

# Alice computes the shared key using Bob's public key
alice_shared_key = alice_private_key.exchange(bob_public_key)

# Bob computes the shared key using Alice's public key
bob_shared_key = bob_private_key.exchange(alice_public_key)

# Verify that Alice's and Bob's shared keys match
if alice_shared_key == bob_shared_key:
    print("Shared keys match. Key exchange successful!")
    print("Shared Key:", alice_shared_key.hex())
else:
    print("Shared keys do not match. Key exchange failed.")
