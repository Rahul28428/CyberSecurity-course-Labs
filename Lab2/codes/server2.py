#Importing the essential libraries
import socket
import os
from _thread import *
#creating a socket object
ser = socket.socket()
host = '127.0.0.1'
port = 2010  #socket server port number
#creating a variable named ThreadCount to count the no. of running processes 
ThreadCount = 0
try:
    ser.bind((host, port)) # bind to the port
except socket.error as e:
    print(str(e))

ser.listen(5) # putting the socket into listening mode
print('Socket is listening..')

def multi_threaded_client(connection):
    connection.send(str.encode('Server is working:'))
    while True:
        data = connection.recv(2048)
        response = 'Server message: ' + data.decode('utf-8')
        if not data:
            break
        s1=data
        res=eval(s1)
        s1_val=str(res)
        connection.sendall(s1_val.encode())   
    connection.close()

while True:
    Client, address = ser.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_threaded_client, (Client, ))
    ThreadCount += 1 #increementing variable






    