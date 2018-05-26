'''
Created on 2018年5月13日

@author: wanyang
    input:从控制台输入,输入后的类型都为字符串
    python数据类型:str,int,long,float,boolean,complex
    数据结构:dict(map),orderdict(有序map),list(list),set(set),tuple(元祖,相当于数据),双向队列(队列),单项队列(栈)
    id(arg):拿到该参数在python内存中的地址
    dir(arg):拿到该参数可以使用的方法
    for in :方法可遍历所有类型的数据,当遍历dic时,是遍历其中的key,遍历dic时可直接写成for k,v in dic
    逻辑判断:and,or,not
    
    定义方法:定义方法的形参,可以直接写变量,也可以写成key=value的形式
    def funcName(args):往方法中传参数时,传递元组用*tuple,传递dic用**dic;
        传递参数时,实参的个数和形参的个数要一样,但是传递元组,或list或dic时,可以不一样,但是要用特定的形式
    def funcName(args,*arg):当实参的个数大于形参的个数,多于的实参会放入*arg中,这是一个元组,arg可自定义
    def funcName(args,**arg):当实参的个数大于形参的个数,且多于的参数是dic时,放入arg中,arg可自定义
    def funcName(args,*arg,**arg):同样是防止参数过多的形式
    
    当执行某故意python文件的时候,可以直接在该文件中取得__name__,入口文件的__name__就是__main__的字符串,
        若是被其他py文件调用,则__name__就是被调用文件的完整路径名

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

str1 = input("输入吧:")
print(str1)

print(__name__)