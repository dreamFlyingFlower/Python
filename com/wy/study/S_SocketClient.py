'''
Created on 2020年2月29日

@author: wanyang
socket使用客户端
'''
import socket

client = socket.socket() # 声明socket类型,同时生成socket连接对象
client.connect(("localhost",12345)) #建立连接
client.send("message".encode("utf-8"))  # 发送信息,必须是bytes类型,若是不带中文,直接前面加b就可以,若带中文,先编码,不能发""和None
data = client.recv(1024)    # 接收消息,socket发送和接收都是bytes类型,发的时候需要encode,接的时候需要decode
print(data.decode("utf-8"))
client.close()