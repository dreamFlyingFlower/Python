"""
定义方法:定义方法的形参数,可以直接写变量,也可以写成key=value的形式
    def funcName(args):传参时,实参的个数和形参的个数要相同,但是传入元组,list,dic时,可以不一样,但是要用特定的形参
    def funcName(args,*arg):当实参的个数大于形参的个数时,多于的实参会放入*arg中,arg是一个元组
    def funcName(args,**arg):当实参的个数大于形参的个数时,若多于的参数是dict,放入**arg中,arg是一个元组
    def funcName(args,*arg1,**arg2):防止参数过多的形式,args必须写在arg1前,arg1必须写在arg2之前,否则编译不通过
        传参时,若实参个数大于形参数,多余的非key1=value2形式的参数全部放入arg1中,key1=value1形式的参数全部放到arg2中
        如:func1(*params1,**params2):->par1=("fds","32432","gdfr"),par2=("fdg","vd"),
        当往func1()中传par1和par2时,par1和par2都会放到params1中,形成一个新的元组(("fds","32432","gdfr"),("fdg","vd")),
        而不是将元组中的数据拿出来,直接形成一个纯元组

    定义类中的方法:必须都自带self,其他的和普通定义方法一样
"""
import copy

ttt=1
tttt=2
print(locals())
print(globals())
print("------")
print(id(tttt))
def tttttt(p1,p2=34):
    """ 你是谁 """ # help(tttttt.__doc__) # 控制台打印tttttt方法的注释
    print(id(p1))
    p1 = 35
    print(id(p1))
    print(str.format("{0}--{1}", p1,p2))
    global ttt
    ttt=3
    print(ttt)
tttttt(tttt)
print(tttt)
str2 = 112
print("--------")
def testtt():
    global str2
    str2 = 45
    print(str2)
testtt()
print(str2)
def test5(t1,t2):
    print(t1,t2)
test5((1,2,3,"r"), {"key1":"value1"})
test5({"key1":"value1"},(1,2,3,"r"))
def test6(*arg2,**arg1):
    print(arg1,arg2)
test6((1,3,4,5),(45,6,7,89),[34,657,8])