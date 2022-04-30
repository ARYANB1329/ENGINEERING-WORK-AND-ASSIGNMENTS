# ARYAN SIDDHABATHULA 121910313029

import socket
port = 5005
s = socket.socket()
host = socket.gethostname()
s.bind((host, port))
s.listen(5)
print('Server listening....')
print("Waiting for connections!!!")
while True:
    client, address = s.accept()
    print('Got connection from', address)
    data = client.recv(1024)
    print('Server received:', data.decode())
    f = open("C:/Users/Aryansid/OneDrive/Desktop/"+str(data.decode())+".txt","rb")
    l = f.read(1024)
    while (l):
       client.send(l)
       print("The Text File has been sent")
       l = f.read(1024)
    f.close()
    print("File Transfer Done")
    client.close()