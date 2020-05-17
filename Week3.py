import socket

mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(("data.pr4e.org",80))

req="GET http://data.pr4e.org/intro-short.txt HTTP/2.0\r\n\r\n".encode()
mysock.send(req)

while True:
    data=mysock.recv(4096)
    if(len(data)<1):
        break
    print(data.decode(),end="")

mysock.close()


