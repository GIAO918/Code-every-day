from socket import *
from time import ctime

HOST = '127.0.0.1'
PORT = 8877
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('wait for connection ....')
    conn_obj, addr = tcpSerSock.accept()
    print(addr)

    while True:
        data = conn_obj.recv(BUFSIZ)
        if data.decode("utf-8") == "quit":
            break
        conn_obj.send("{}发送了：{}".format(ctime(), data.decode("utf-8")).encode("utf8"))

    conn_obj.close()

    tcpSerSock.close()
