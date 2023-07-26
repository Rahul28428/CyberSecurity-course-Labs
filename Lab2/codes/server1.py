#Importing the socket library
import socket

HOST = "127.0.0.1"  
PORT = 2002  #socket server port number

#creating a socket object and passing two parameters to it
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as ser: 

#AF_INET refers to the address family ipv4
# SOCK_STREAM refers to onnection-oriented TCP protocol


    ser.bind((HOST, PORT)) # bind to the port
    ser.listen() # putting the socket into listening mode
    print('Socket is listening..')
    connection, addr = ser.accept()  # establishing connection with client
    with connection:
        print(f"Connected by {addr}")
        #running a infinite loop until we interrupt or error occurs
        while True:
            data = connection.recv(1024)
            if not data:
                break
            s1=data
            res=eval(s1)  # eval solves mathematical expressions 
            s1_val=str(res) # passing a string to eval
            connection.sendall(s1_val.encode()) # Encoding to send byte type