import socket
import random

prime = 42809
r = 3

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 5829)
print(f"Connecting to {server_address[0]} port {server_address[1]}")
sock.connect(server_address)

random = random.randint(1, prime-1)

M = pow(r, random, prime)
#print(f"Sending A = {A} to the server")
sock.sendall(str(M).encode())

data = sock.recv(1024)
B = int(data.decode())
#print(f"Received B = {B} from the server")

s = pow(B, random, prime)
print(f"Shared secret key: {s}")

message = "My name is Rahul"
encrypted_message = ""
for char in message:
    encrypted_char = chr(ord(char) ^ s)  # XOR the character with the shared secret key
    encrypted_message += encrypted_char
print(f"Encrypted message: {encrypted_message}")

sock.sendall(encrypted_message.encode())

sock.close()
