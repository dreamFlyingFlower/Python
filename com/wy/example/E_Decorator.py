'''
Created on 2020年2月26日

@author: wanyang
注解方法:
    1.方法A为注解方法,其参数为一个方法指针,方法B为需要添加A注解的方法,调用B方法的时候就相当于调用A方法
        该方式在调用B方法的时候不需要写(),直接写B就行,有点怪异,不建议这样调用
    2.同1,只是并不直接调用参数B,而是在A方法内部再增加一个方法,返回A的内部方法,内部方法调用B,此时B就是正常调用
'''

def A(func):
    print("before")
    func()
    print("after")
    
    def warpper(*arg1,**arg2):
        print(arg1)
        print(arg2)
        print("wrapper before")
        func()
        print("wrapper after")
    return warpper
@A
def B():
    print("B")
    
# B   # 加上()会报错,不推荐使用
B()