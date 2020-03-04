'''
Created on 2020年2月28日

@author: wanyang
一个简单的键值对内存数据存储到文件的模块,可以持久化任何pickle可支持的python数据格式
'''
import shelve

file = shelve.open("testFile")  # 默认会创建3个文件,后缀分别是bak,dat,dir
file["test"]=[23,54]    # 只能通过属性或update方法添加属性,关闭文件时写入到文件中
file["eee"]=34
file.close()
file = shelve.open("testFile")
print(file.get("test")) # 直接读取内容
