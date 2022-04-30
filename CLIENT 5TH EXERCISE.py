# ARYAN SIDDHABATHULA 121910313029

import socket
import os
client = socket.socket()
host = socket.gethostname()
port =5005
t=0
client.connect((host, port))
z1=input("Enter a File name to get from the server:")
client.sendall(bytes(z1,'utf-8'))
with open('client', 'wb') as f:
    while True:
        data = client.recv(1024)
        if data:
            t=1
            print('file  opened')
            print('receiving the data')
            print((data).decode())
            print('Successfully file has been received')
            f.write(data)
            break
        break
if t!=1:
    os.remove('client')
    print("data not found")
    print("Unsuccesful")
f.close()
client.close()
print('connection closed')