# ARYAN SIDDHABATHULA 121910313029

import socket
c=socket.socket()
c.connect(('localhost', 5003))
print(c. recv(1024))
c.sendall(bytes('HeyAryan! I am the client!','utf-8'))
c.close()
