from Crypto.Cipher import DES
import hashlib
import os

# Generate a 64-bit (8-byte) key from given string B20CS047RAHUL
input_str = "B20CS047RAHUL"
input_bytes = input_str.encode()
key = hashlib.sha256(input_bytes).digest()[:8]

# Create a DES cipher object
cipher = DES.new(key, DES.MODE_ECB)

message = b'My name is Rahul'
ciphertext = cipher.encrypt(message)

decrypted_msg = cipher.decrypt(ciphertext)

print('Plaintext:', message)
print('Ciphertext:', ciphertext)
print('Decrypted:', decrypted_msg)