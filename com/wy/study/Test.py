'''
Created on 2018年5月13日

@author: wanyang

    twisted框架暂不支持python3,只是还没修改完,现在是否支持,可查官网,类似于httpclient
    input:从控制台输入,输入后的类型都为字符串
    python数据类型:str,int,long,float,boolean,complex
    数据结构:dict(map),orderdict(有序map),list(list),set(set),frozenset(不可变集合),tuple(元祖,相当于数据),双向队列(队列),单项队列(栈)
    chr(x):将整数转换为单字符
    ord(x):将字符转换为整数
    hex(x):将整数转为16进制字符串
    bin(x):将整数转为2进制
    oct(x):将整数转为8进制
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
    在往方法中传值的时候,若传递的是元组和dic,元组的参数必须写在dic的参数前面,否则报错
        若是其他单个的参数则必须写在元组的前面
        往方法中传参数的时候,若是将需要传的值赋值给一个变量,而接收这个这个变量的形参是一个元组,则会将多个变量全部放到一个形参中
        例如:par1=("fds","32432","gdfr"),par2=("fdg","vd"),
        func1(*params1,**params2):
        当往func1(par1,par2)中如此传参时,par1和par2都会放到params1中,形成一个新的元组(("fds","32432","gdfr"),("fdg","vd"))
        而不是将元组中的数据拿出来,直接形成一个纯元组
    
    定义类中的方法:必须都自带self,其他的和普通定义方法一样
    
    
    当执行某故意python文件的时候,可以直接在该文件中取得__name__,入口文件的__name__就是__main__的字符串,
        若是被其他py文件调用,则__name__就是被调用文件的完整路径名

    深浅拷贝:深拷贝就是重新开辟一块内存放入新的变量,浅拷贝就是都有原变量的地址
    
    异常:
    try: 
    except Exception,e: 
    finally:
    方法或其他需要进行操作的地方,若不进行操作,可使用pass关键字,但是不能什么都不写,会报错
    
    pickle:序列化
    
    异常,日志,python自带,但是不知道有没有框架,可网上查找
    
    zip:将2个元组强行合并成一个类似map一样的组成的元组,可以强制转换为list,可以用enumerate迭代,
        使用enumerate对一个数组或list或map进行迭代的时候会返回一个类似map的对象
        第一个参数是array或list中的元素在列表中的位置,第二个参数是元素的值
        用zip转换的元组,若元组个数不同,以短的为准,多个舍弃
        
    __init__:每个包下面自动生成的__init__文件,可以让该包中的所有文件都能被其他包导入使用,如果没有这个文件
        其他包将无法使用该包下的文件,在每个文件中都会有一个内置的__init__,当直接指定该文件的使用,
        __init__=="__main__",当该文件是被其他文件调用的使用,__init__等于该文件的名称
    __all__:写在自动生成的__init__文件中,以元组的形式,写入可以导入的包名,只要不在这个元组里的,即使导入也无法使用类里的方法

    制作一个可以安装到系统的自己的模块:往上查找,需要先制作一个安装包,然后打包之后安装,之后可以像系统自带的
        包一样,直接在任务python中用import引入
        
    在一个方法里面不能修改一个基本类型全局变量,包括str,必须要加上global,例如global a,之后才可以修改.
        否则只能引用,但是可以直接修改对象
        当这个基本类型当作参数传递到方法里时,是可以修改的,但是只在该 方法内改变参数,不影响全局
    在方法里面对参数进行运算时,a+=a,和a=a+a是不一样的结果,后一种是先定义一个变量,已经不再是传递的参数
        的地址值,这跟java里很不一样,可变性太多,因为java里的元组等不能使用+=运算,但是python中各种类型都可以
        
    //:整除
    **:幂运算
    逻辑运算符:and,or,not相当于&&,||,!
    判断一个元组中的成员,用in的时候可以使用not in,不存在而不是not param in typle
    is和is not判断某一个变量是否为某类型,需要使用type,ex:type(tuple) is tuple 为True
'''
#!/usr/bin/env python
from _functools import reduce

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

#可定义对应个数的参数直接取出元组或数组的参数,并赋值到变量上
aa,bb,cc=["fdsf","fdsgfd","gfdg"]
#dict的遍历,可遍历key,可遍历value,也可遍历items,遍历items得到的是一个元组
map1 = {"id1":11}
for x,y in map1.items():
    print("%s,%s" %(x,y))
    
print(type(map1) is dict)

#lambda表达式,需要关键字lamba,并且用一个变量接受,类似js中的变量方法
l = lambda x,y:x*y;
#调用lambda函数
l(5,6);

listArr = [1,2,34,56,6];
#reduce函数类似于递归,第一个参数可以是一个方法,第一个参数是方法作用的列表
#第一个参数会从list中拿值作为第一个参数的参数,然后将返回值作为参数,继续和下一个参数进行运算
#直到list的走完
reduce(lambda x,y:x*y,listArr);