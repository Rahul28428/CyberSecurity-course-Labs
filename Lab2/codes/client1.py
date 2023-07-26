#Importing the socket library
import socket
HOST = "127.0.0.1" 
PORT = 2002  #socket server port number

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as ser:
    ser.connect((HOST, PORT))  #connecting to the server
    comm=input("Enter the expression:") #asking for input expression
    ser.sendall(bytes(comm,encoding='utf8'))
    data = ser.recv(1024)

print(data.decode('utf-8')) #print the ans from server

