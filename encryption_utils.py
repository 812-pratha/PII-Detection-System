from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def encrypt_text(key, plaintext):
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv
    plaintext = plaintext.encode("utf-8")
    padded_plaintext = plaintext + b"\0" * (16 - len(plaintext) % 16)
    ciphertext = cipher.encrypt(padded_plaintext)
    return iv + ciphertext

def decrypt_text(key, ciphertext):
    iv = ciphertext[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_plaintext = cipher.decrypt(ciphertext[16:]).rstrip(b"\0")
    return decrypted_plaintext.decode("utf-8")
