'''
Created on 2020年2月29日

@author: wanyang
socket使用服务端,
socket要注意粘包,就是同一方连续发送2条数据,2条数据的内容粘在一起发送,解决办法,在两条发送信息中间插入一条接收信息
SocketServer:和socket类似,稍微比socket简单,但是需要自定义其中的handler方法,同时可以使用ThreadTCPServer来进行多线程通讯
'''
import socket
import socketserver

server = socket.socket() # 声明socket类型,同时生成socket连接对象
server.bind(("localhost",12345))    # 绑定监听端口
server.listen() # 开始监听,若listen带参数,表示允许多少连接同时排队等待
'''
等待其他程序连接,会返回2个值,第一个是其他程序的连接对象,第2个是其他程序的ip
每个程序连接到服务器都会产生一个实例,每个实例不同,后面的操作都是通过这个实例来完成
'''
client,addr = server.accept()   # 等待其他程序连接
data = client.recv(1024)    # 接收信息
print(data)
client.send("发信息回去".encode("utf-8"))    # 再发信息回去,不能发""和None

server.close()

class TestSocketServetHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            data = self.request.recv(1024).strip()
            print(data)
            self.request.send("yes,this is the data")
if __name__ == "__main__":
    HOST,PORT = "localhost",9999
    server = socketserver.ThreadingTCPServer((HOST,PORT),TestSocketServetHandler)
    server.serve_forever()
