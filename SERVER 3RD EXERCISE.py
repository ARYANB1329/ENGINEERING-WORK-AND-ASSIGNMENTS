# ARYAN SIDDHABATHULA 121910313029

import socket
s=socket.socket()
print("Socket Created")
s.bind(('localhost',5003))
s.listen(3)
print('Waiting for connections')
while True:
    c,addr=s.accept()
    print("Connected with:",addr)
    c.send(bytes('Hey Aryan,I am server','utf-8'))
    print(c.recv(1024))
    c.close()