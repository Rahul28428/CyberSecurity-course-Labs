from Crypto.Cipher import DES
import os

# Generate a random 64-bit key for DES
key = os.urandom(8)

# Define a function to encrypt a message using DES with CFB mode
def encrypt(message):
    iv = os.urandom(8)
    cipher = DES.new(key, DES.MODE_CFB, iv)
    ciphertext = cipher.encrypt(message)
    return ciphertext, iv

# Define a function to decrypt a message using DES with CFB mode
def decrypt(ciphertext, iv):
    cipher = DES.new(key, DES.MODE_CFB, iv)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

# Test the encryption and decryption functions with a sample message
message = b'My name is Rahul'
ciphertext, iv = encrypt(message)
print('Ciphertext:', ciphertext.hex())
plaintext = decrypt(ciphertext, iv)
print('Plaintext:', plaintext)
