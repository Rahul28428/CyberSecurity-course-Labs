# Define a function to encrypt a message using DES with CBC mode
def encrypt(message):
    iv = os.urandom(8)
    cipher = DES.new(key, DES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(message)
    return ciphertext, iv

# Define a function to decrypt a message using DES with CBC mode
def decrypt(ciphertext, iv):
    cipher = DES.new(key, DES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

# Test the encryption and decryption functions with a sample message
message = b'This is a secret message.'
ciphertext, iv = encrypt(message)
print('Ciphertext:', ciphertext.hex())
plaintext = decrypt(ciphertext, iv)
print('Plaintext:', plaintext)



