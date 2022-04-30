from socket import *
serverPort=5009
hostname = "127.0.0.1"
soc=socket(AF_INET, SOCK_DGRAM)
soc.bind((hostname,serverPort))
n=int(input('Enter no.of clients :\n'))
print('The server is ready to receive....')
c=0
while True:
    text,ca=soc.recvfrom(1024)
    c+=1
    text=text.decode('utf8')
    try:
        f=open(text,"rb")
        l=f.read()
        print('client -{} asked for {}'.format(c,text))
        print("Sending file ",text)
        soc.sendto(l,ca)
        print("File sent")
    except:
        print('file {} not found'.format(text))
    f.close()
    if c==n:
        print('........all the necessary files have been sent....')
        break
soc.close()