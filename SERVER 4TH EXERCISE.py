# ARYAN SIDDHABATHULA 121910313029

import socket
server = socket.socket()
server.bind(("localhost", 5003))
server.listen(2)
client, address = server.accept()
print(str(address) + "")
while True:
    clientMessage = client.recv(1024).decode()
    if len(clientMessage) == 0 :
        print("Connection Lost")
        break
    else:
        print("client : "+ clientMessage)
        serverMessage = input("Enter :")
        client.send( serverMessage.encode())
server.close()