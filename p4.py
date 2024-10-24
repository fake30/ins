# Digital signature (RSA)
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

# Generate RSA key pair (2048 bits)
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# Serialize the private key to PEM format
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

# Save private key to a file
with open("private_key.pem", "wb") as f:
    f.write(private_pem)

# Get the corresponding public key
public_key = private_key.public_key()

# Serialize the public key to PEM format
public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Save public key to a file
with open("public_key.pem", "wb") as f:
    f.write(public_pem)

# Load the public key from a file
with open("public_key.pem", "rb") as f:
    public_pem = f.read()
    public_key = serialization.load_pem_public_key(public_pem)

# Load the private key from a file
with open("private_key.pem", "rb") as f:
    private_pem = f.read()
    private_key = serialization.load_pem_private_key(private_pem, password=None)

# Message to be encrypted
plaintext = b"Hello, RSA!"

# Encrypt the message with the public key
ciphertext = public_key.encrypt(
    plaintext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Decrypt the message with the private key
decrypted_text = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("Original Message:", plaintext.decode())
print("Encrypted Message:", ciphertext.hex())
print("Decrypted Message:", decrypted_text.decode())
