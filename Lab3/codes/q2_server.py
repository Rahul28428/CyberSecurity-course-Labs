import socket

prime = 42809
r = 3

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ser_add = ('localhost', 5829)
#print(f"Starting up on {ser_add[0]} port {ser_add[1]}")
sock.bind(ser_add)

sock.listen(1)

while True:
    print("Waiting for a connection...")
    conc, client_address = sock.accept()

    try:
        data = conc.recv(1024)
        M = int(data.decode())
        #print(f"Received A = {A} from the client")

        random = 12345

        B = pow(r, random, prime)
        #print(f"Sending B = {B} to the client")
        conc.sendall(str(B).encode())

        s = pow(M, random, prime)
        print(f"Shared secret key: {s}")

        data = conc.recv(1024)
        enc_msg = data.decode()
        print(f"The received encrypted message is: {enc_msg}")

        msg = ""
        for char in enc_msg:
            decrypted_char = chr(ord(char) ^ s)  # XOR the character with the shared secret key
            msg += decrypted_char
        print(f"The decrypted message is : {msg}")

    finally:
        conc.close()
