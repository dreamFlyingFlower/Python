# 利用gevent进行socket的使用
import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 9999))
while True:
    msg = bytes(input(">>:"), encoding="utf8")
    client.sendall(msg)
    data = client.recv(1024)
    print('Received', data)
client.close()
