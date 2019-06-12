from socket import *

HOST = "127.0.0.1"
PORT = 8877
BUFSIZ = 1024
ADDR = (HOST,PORT)

tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect_ex(ADDR)

while True:
    data = input("输入文字或者quit退出>:")
    if not data:
        print("输入不能为空,请重新输入")
        continue
    tcpCliSock.send(data.encode("utf8"))
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data.decode("utf-8"))
tcpCliSock.close()
