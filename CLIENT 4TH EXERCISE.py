# ARYAN SIDDHABATHULA 121910313029

import socket
Client = socket.socket()
Client.connect(("localhost", 5003))
print("")
while True:
    clientMessage = input("enter message: ")

    if clientMessage == "bye":
        print("connection lost")
        break
    else:
        Client.send(clientMessage.encode())
        serverMessage = Client.recv(1024).decode()
        print("Server: "+serverMessage)
Client.close()