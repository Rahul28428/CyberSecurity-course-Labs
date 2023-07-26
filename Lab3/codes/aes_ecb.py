from Crypto.Cipher import AES
import os

# Convert the input string to bytes
input_str = "B20CS047RAHUL"
input_bytes = input_str.encode()

# Pad the input bytes with zeroes to the right until it reaches 16 bytes
key = input_bytes.ljust(16, b'\x00')


# Define a function to pad the message to a multiple of 16 bytes
def pad_message(message):
    padding_length = 16 - (len(message) % 16)
    padding = bytes([padding_length] * padding_length)
    return message + padding

# Define a function to unpad the message after decryption
def unpad_message(message):
    padding_length = message[-1]
    return message[:-padding_length]

# Define a function to encrypt a message using AES with ECB mode
def encrypt(message):
    padded_message = pad_message(message)
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(padded_message)
    return ciphertext

# Define a function to decrypt a message using AES with ECB mode
def decrypt(ciphertext):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_message = cipher.decrypt(ciphertext)
    plaintext = unpad_message(padded_message)
    return plaintext

# Test the encryption and decryption functions with a sample message
message = b'My name is Rahul'
ciphertext = encrypt(message)
print('Ciphertext:', ciphertext.hex())
plaintext = decrypt(ciphertext)
print('Plaintext:', plaintext)
