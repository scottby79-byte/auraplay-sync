import os
from cryptography.fernet import Fernet

# It's crucial that this key is set as an environment variable and is a 32-byte URL-safe base64-encoded string.
# You can generate a key using: `openssl rand -base64 32`
ENCRYPTION_KEY = os.environ.get("ENCRYPTION_KEY")
if not ENCRYPTION_KEY:
    raise ValueError("No ENCRYPTION_KEY set for Flask application")

cipher_suite = Fernet(ENCRYPTION_KEY.encode())

def encrypt_data(data: str) -> str:
    """Encrypts a string."""
    if not data:
        return ""
    return cipher_suite.encrypt(data.encode()).decode()

def decrypt_data(encrypted_data: str) -> str:
    """Decrypts a string."""
    if not encrypted_data:
        return ""
    return cipher_suite.decrypt(encrypted_data.encode()).decode()
