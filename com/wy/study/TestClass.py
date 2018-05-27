'''
Created on 2018年5月27日
@author: wanyang
    定义类的时候的时候继承object,可调用新的方法,成为新型对象类,不继承object是普通类
    类中定义的方法必须传一self,相当于java中的this,但是调用的时候不需要传
    继承:在定义类的时候,后面的括号中可以写需要继承的类名,可多继承,写过个父类
        若多继承的父类中有冲突的公有属性和方法,都以继承的顺序中的第一个为准
        除非子类重写了父类的相同属性和方法
'''
#类外的属性,没什么用处
str1 = " w ye bu zd";

class TestClass(object):
    
    #属性,必须赋值,公有属性,相当于java中的static和public相结合
    #公有属性可以直接以类名点属性名,TestClass.str1,不是调用的类外属性,谨慎,容易出错,最好不要用
    #若是用类型.属性调用的话,这个属性不会引文多个对象改变该对象而改变,他只会是初始化的值
    str1 = "里面的";
    num1 = 0;
    #私有属性,__username,username自定义,在属性前面加2个下划线
    #私有属性,不能直接调用,但是内置的系统属性可以直接调用
    __username = "that";
    __age=0;
    #系统内置属性,就是系统关键字之类的比如__name__
    
    #必须要传一个self(可自定义),但实体类调用的时候不需要传self,就是类本身
    #不论是公有方法还是私有方法都不能直接被类名.方法名调用
    def test(self):
        #访问的是类外的str1,若要访问类里的str1,需要加上self
        print(str1);
        print(self.str1);
        #必须要有具体的实现,没有也不能不写,必须写pass
#         pass
    #私有方法
    def __test01(self):
        print("test01");
    #将一个公有方法或私有方法变为一个可被类名.方法名调用的方法
    #主要的调用相当于继承
    func1 = classmethod(test);
    #私有方法可同公有方法一样被类化
    func2 = classmethod(__test01);
    
    #语法报错,但是运行不会报错,需要网上找资料,不过用注解的方式更好
    def test02():
        print("静态方法测试")
    
    #静态方法,被调用的方法不可传self,和类化方法没什么不同,除了执行时候的内存加载
    func3 = staticmethod(test02);
    
    #方法变为类化或静态也可以使用注解
    @classmethod
    def test03(self):
        print("test03")
    
    @staticmethod
    def test04():
        print("test04")
    
if __name__ == "__main__":
    O1 = TestClass();
    O2 = TestClass();
    #当对象已经定义了之后,可以直接在对象上添加任何想要的属性,跟js的Object一样
    O1.FSDFDS= "fdsfgd";
    O1.str1 = "trest1";
    print(O1.str1)#trest1
    O2.str1="gfdgfdg";
    print(O2.str1)#gfdgfdg
    print(TestClass.str1)#里面的
    TestClass.func1();#类名直接调用方法
    print("#"*5)
    TestClass.func2();
    TestClass.func3();
    TestClass.test04();