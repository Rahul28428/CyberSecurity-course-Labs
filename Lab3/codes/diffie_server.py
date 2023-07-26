import socket

# agreed upon values
p = 65537
g = 3

# create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to a specific address and port
server_address = ('localhost', 10000)
print(f"Starting up on {server_address[0]} port {server_address[1]}")
sock.bind(server_address)

# listen for incoming connections
sock.listen(1)

while True:
    # wait for a connection
    print("Waiting for a connection...")
    connection, client_address = sock.accept()

    try:
        # receive g^a mod p from the client
        data = connection.recv(1024)
        A = int(data.decode())
        print(f"Received A = {A} from the client")

        # generate a random secret number
        b = 12345

        # send g^b mod p to the client
        B = pow(g, b, p)
        print(f"Sending B = {B} to the client")
        connection.sendall(str(B).encode())

        # calculate the shared secret key
        s = pow(A, b, p)
        print(f"Shared secret key: {s}")

        # receive the encrypted message from the client
        data = connection.recv(1024)
        encrypted_message = data.decode()
        print(f"Received encrypted message: {encrypted_message}")

        # decrypt the message using the shared secret key
        message = ""
        for char in encrypted_message:
            decrypted_char = chr(ord(char) ^ s)  # XOR the character with the shared secret key
            message += decrypted_char
        print(f"Decrypted message: {message}")

    finally:
        # close the connection
        connection.close()
