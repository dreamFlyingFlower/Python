'''
Created on 2018年5月13日

@author: wanyang
    python数据类型:str,int,long,float,boolean,complex
    数据结构:dict(map),orderdict(有序map),list(list),set(set),tuple(元祖,相当于数据),双向队列(队列),单项队列(栈)
    dir(var):查询一个变量能有那些方法

'''
#!/usr/bin/env python

# python的源码格式为py,编译后的为pyc,经过优化的为pyo
# 编译
# import py_compile
# py_compile("study")
# 优化
# python -O -m py_compile study.py

a=1
print(a)
b="re"
print(b+str(a))
# 拿到a的内存地址值,是python的虚拟内存地址
id(a)
#'''3个单引号或双引号里可使用制表符
print('''d,
        fdsfd
        dsfdwe
''')