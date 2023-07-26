#Importing the socket library
import socket

mul = socket.socket() #creating a socket object

host = '127.0.0.1'
port = 2010  #socket server port number
print('Waiting for connection response')
try:
    mul.connect((host, port))
except socket.error as err:
    print(str(err))
res = mul.recv(1024)

while True:
    Input = print('Enter your expression:')
    mul.send(str.encode(Input))
    res = mul.recv(1024)
    print(res.decode('utf-8'))
mul.close()  #close the connection




