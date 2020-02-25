'''
Created on 2018�?6�?8�?

@author: wanyang

    pickle:json序列化工�?,python独有,和json�?大的不同�?:pickle可以将方�?,对象等等都序列化,并且还能拿出�?
        如果pickle将方法序列化,则在另外�?个文件中拿出这个方法的时�?,�?要在该文件中定义同名方法,实现可以不一�?,但是方法名必须一�?
        用pickle序列化的时�?�只能用wb这种模式,写入二进制文�?,但是pickle不能和其他语�?交互,这时候就只能用json
        
    json:json序列化工�?,和pickle有同样的方法,但是json无法使用wb的写入模�?,只能是字符串
'''
import pickle
import json

dict1 = {"key1":"test1", "key2":"test2"}
file = open("testFile.txt", "wb")
# 将数据序列化之后存入文件�?
data = pickle.dumps(dict1);
file.write(data);
file.close();
# json的用法和pickle是一样的,只是不能存入和读取二进制
# file = open("testFile.txt", "w")
# data = json.dumps(dict1);
# file.write(data);
# file.close();

# 直接将dict类型写入文件�?,不需要显式的调用dumps方法,文件也不�?要写write和close
# pickle.dump(dict1, file);

file = open("testFile.txt", "rb")
# data = file.read();
# file.close();
# fff =pickle.loads(data);
# print(fff)

des = pickle.load(file);
print(des)
# json只能读取字符�?,不能读取二进制文�?
json.load(file)
