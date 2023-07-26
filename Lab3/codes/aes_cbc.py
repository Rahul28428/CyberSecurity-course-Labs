from Crypto.Cipher import AES
import os
from Crypto.Util.Padding import pad, unpad

# Convert the input string to bytes
input_str = "B20CS047RAHUL"
input_bytes = input_str.encode()

# Pad the input bytes with zeroes to the right until it reaches 16 bytes
key = input_bytes.ljust(16, b'\x00')
iv = os.urandom(16)

# Define a function to encrypt a message using AES with CBC mode
def encrypt(message):
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    ciphertext = cipher.encrypt(pad(message, AES.block_size))
    return ciphertext

# Define a function to decrypt a message using AES with CBC mode
def decrypt(ciphertext):
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext

# Test the encryption and decryption functions with a sample message
message = b'My name is Rahul'
ciphertext = encrypt(message)
print('Ciphertext:', ciphertext.hex())
plaintext = decrypt(ciphertext)
print('Plaintext:', plaintext)
