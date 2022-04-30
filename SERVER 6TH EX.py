import socket
server = socket.socket()
server.bind(("localhost", 5006))
server.listen(3)
print("Server Activated")
while True:
    client, address = server.accept()
    print(str(address)+" is connected.")
    client_request = client.recv(1024)
    filename = client_request
    f = open(filename,'rb')
    l = f.read(1024)
    client.send(l)
    f.close()
    print(" File Sent to  " + str(address) + " server !")
server.close()