import base64
import hashlib
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def derive_key(MasterPassword: str) -> bytes:
    return hashlib.sha256(MasterPassword.encode()).digest()

def encrypt_password(plainText: str, MasterPassword: str) -> str:
    key = derive_key(MasterPassword)
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CFB, iv)
    encrypted = cipher.encrypt(plainText.encode())
    return base64.b64encode(iv + encrypted).decode()

def decrypt_password(encoded: str, MasterPassword: str) -> str:
    raw = base64.b64decode(encoded)
    iv = raw[:16]
    encrypted = raw[16:]
    key = derive_key(MasterPassword)
    cipher = AES.new(key, AES.MODE_CFB, iv)
    decrypted = cipher.decrypt(encrypted)
    return decrypted.decode()
