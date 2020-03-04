'''
Created on 2020年2月27日

@author: wanyang
json的序列化和反序列化
json:序列化工具,和pickle有同样的方法,但是json无法使用wb的写入模式,只能写字符串
pickle:和json不同的是可以将方法,对象,类等都进行序列化,但只写入文件时只能用wb这种带二进制的模式.
    pickle写入文件的json数据不能和其他语言交互,此时只能用json序列化
    pickle将写入到文件中的方法取出来时,调用pickle的模块必须有同名的方法定义,方法体不可以不一样
'''
import pickle
import json

dict1 = {"key1":"test1", "key2":"test2"}
file = open("testFile.txt", "w+",encoding="utf8")# json的用法和pickle是一样的,只是不能存入和读取二进制
data = json.dumps(dict1);
print(type(data));  # dumps之后得到的是字符串
file.write(data)
file.close()  # flush之后无法立刻读,仍然有缓存
file = open("testFile.txt", "r",encoding="utf8")  # json只能读取字符串,不能读取二进制文件
data1 = json.loads(file.read())
print(type(data1))  # dict
file.close()
file = open("testFile.txt", "r",encoding="utf8")
data2 = json.load(file)  # 其实仍然是调用json.loads(file.read())
file.close()

# 读取文件中的json字符串,并转换
file1 = open("testFile.txt", "rb+")
file1.write(pickle.dumps(dict1))    # 不管是以何种形式打开文件,pickle读取的都是bytes类型
# pickle.dump(dict1, file);# 直接将dict类型写入文件中,不需要显式的调用dumps方法,文件也不需要写write和close
file1.close();
file1 = open("testFile.txt", "rb+")
data = file1.read();
print("-----",pickle.loads(data))
file1.seek(0)
des = pickle.load(file1);
print(des)
file1.close();