'''
Created on 2018年6月8日

@author: wanyang

    pickle:json序列化工具,python独有,和json最大的不同是:pickle可以将方法,对象等等都序列化,并且还能拿出来
        如果pickle将方法序列化,则在另外一个文件中拿出这个方法的时候,需要在该文件中定义同名方法,实现可以不一样,但是方法名必须一样
        用pickle序列化的时候只能用wb这种模式,写入二进制文件,但是pickle不能和其他语言交互,这时候就只能用json
        
    json:json序列化工具,和pickle有同样的方法,但是json无法使用wb的写入模式,只能是字符串
'''
import pickle
import json

dict1={"key1":"test1","key2":"test2"}
file = open("testFile.txt", "wb")
# 将数据序列化之后存入文件中
data = pickle.dumps(dict1);
file.write(data);
file.close();
#json的用法和pickle是一样的,只是不能存入和读取二进制
# file = open("testFile.txt", "w")
# data = json.dumps(dict1);
# file.write(data);
# file.close();

#直接将dict类型写入文件中,不需要显式的调用dumps方法,文件也不需要写write和close
# pickle.dump(dict1, file);

file = open("testFile.txt", "rb")
# data = file.read();
# file.close();
# fff =pickle.loads(data);
# print(fff)

des = pickle.load(file);
print(des)
#json只能读取字符串,不能读取二进制文件
json.load(file)