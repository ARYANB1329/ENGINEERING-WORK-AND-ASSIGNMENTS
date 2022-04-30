import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.sendto(bytes(input("Enter filename: "), "utf-8"),("localhost",5009))

newname= input("Enter new filename : ")

f = open(newname, "wb")

data, addr = sock.recvfrom(1024)

f.write(data)

f.close()
