import socket
import random

# agreed upon values
p = 65537
g = 3

# create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
server_address = ('localhost', 10000)
print(f"Connecting to {server_address[0]} port {server_address[1]}")
sock.connect(server_address)

# generate a random secret number
a = random.randint(1, p-1)

# send g^a mod p to the server
A = pow(g, a, p)
print(f"Sending A = {A} to the server")
sock.sendall(str(A).encode())

# receive g^b mod p from the server
data = sock.recv(1024)
B = int(data.decode())
print(f"Received B = {B} from the server")

# calculate the shared secret key
s = pow(B, a, p)
print(f"Shared secret key: {s}")

# encrypt a message using the shared secret key
message = "Hello, server!"
encrypted_message = ""
for char in message:
    encrypted_char = chr(ord(char) ^ s)  # XOR the character with the shared secret key
    encrypted_message += encrypted_char
print(f"Encrypted message: {encrypted_message}")

# send the encrypted message to the server
sock.sendall(encrypted_message.encode())

# close the socket
sock.close()
