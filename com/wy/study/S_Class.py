'''
    定义类的时候要继承object,可调用新的方法,成为新型对象,不继承object是普通类
    类中定义的方法必须传参数self,相当于java中的this,但是调用的时候不需要传
    继承:在定义类的时候,后面的括号中可以写需要继承的类名,可多继承,写多个父类
        若多继承的父类中有冲突的公有属性和方法,都以继承的顺序中的第1个为准,除非子类重写了父类的相同属性和方法
        子类调用父类的方法,同样是用super,也可以直接父类.方法名
        但是super调用可以不传self,父类.方法名需要传self
    python没有方法的重载,只要名字相同就只能有1个方法,后面的方法覆盖前面的方法
    
    利用正则找网页里的图片re.findall(r'src="(.*?\.(jpg|png|jepg))"',html)
'''
# 类外的属性,没有太大的用处,还容易出问题,建议不要使用
str1 = " w ye bu zd"
str2 = 112


def testtt():
#     print(str2)
    # 先从函数中找,若先调用后定义报错,若没有定义,从包裹函数的外层找,一层一层的找,知道文件末尾,找不到抛异常
    # 此处的修改只对函数内有效,其实只是在函数内重新定义了一个同名变量而已,并不会影响外层变量
    # 要想对外层变量产生影响,需要先使用global关键字修饰
    # 若外层没有定义str2,如使用global修饰了,那么str2就变成了全局变量,但是这很容易会导致全局变量混乱,最好不要用
    global str2
    str2 = 45   
    print(str2)

     
testtt()
print(str2)


class Test():
    
    __slots__=["test"]
    
    def __init__(self):
        print("Parent Test")
        
# tt123 = Test()
# tt123.fdsfew=45 # 抛异常
# print(tt123)
        
# object是所有类的父类,不写默认继承object
class TestClass(Test, object):
    __slots__ = ["test1", "test2"] # 若不继承Test,那么给实例新增不在列表中的值属性时会抛异常

    """
        类全局变量必须赋值,相当于java中的public static
        类全局变量可以直接以类名点属性名,TestClass.str1,不是调用的全局变量,谨慎,容易出错,最好不要用
        直接用类名.属性名或实例.属性名都可以方法类全局变量,但是只能是类名.属性名的时候可以修改类全局变量,
        实例只可访问,不能直接修改类全局变量,但是可以修改可变参数的元素
    """
    str1 = "类全局变量";
    num1 = 6666666666;
    str2 = 456
    print(str2)
    str3 = "大大"
    
    # 私有属性,在属性前面加2个下划线,不能像类全局变量一样外部访问,必须通过方法类中方法访问或内置系统属性调用
    # 类实例._TestClass__username同样可以在外部访问类私有属性,实例属性同样如此
    __username = "that";
    __age = 0;
    # 系统内置属性,就是系统关键字之类的比如__name__
    
    def getUsername(self):
        return TestClass.__username
    
    # 构造方法,self必须是第一个参数,后面的都是参数,self相当于类本身.每次都会调用
    def __init__(self, *args1, **args2):
        # 赋值给类中属性,该属性可以不先定义
        super().__init__()
        Test.__init__(self)
        self.args1 = args1
        self.args2 = args2
        print("我是每次默认都会调的,初始化方法,相当于空构造")
        print(args1)
        TestClass.num1 += 1
        TestClass.str3 = "小小"
        self.testGlobal()
    
    def testGlobal(self):
#         print(str2) # 错误,无法访问module中的全局变量
#         str2 = 5  # 错误,无法修改module中的全局变量
        global str2
        str2 = 10
        print(str2)
        
    def __str__(self, *args, **kwargs):
        print(self.args1)
        print("相当于java里的tostring方法重写,和init一样是内置方法,还有很多,可官网查询")
        return object.__str__(self, *args, **kwargs)
    
    def __del__(self):
        print("相当于destory,对象被销毁时调用,可不重写")
        
    def __call__(self, *arg1, **arg2):
        print(arg1, arg2)
        print("这是一个可调用类")
        print("只需要简单的重写该方法,即可以让类像函数一样调用")
        
    # 必须要传一个self(可自定义),但实体类调用的时候不需要传self,就是类本身
    # 不论是公有方法还是私有方法都不能直接被类名.方法名调用
    def test(self):
        # 访问的是类外的str1,若要访问类里的str1,需要加上self
        print(str1);
        print(self.str1);

    # 私有方法
    def __test01(self):
        print("test01");

    # 将一个公有方法或私有方法变为一个可被类名.方法名调用的方法
    # 主要的调用相当于继承
    func1 = classmethod(test);
    # 私有方法可同公有方法一样被类化
    func2 = classmethod(__test01);
    
    # 语法报错,但是运行不会报错,需要网上找资料,不过用注解的方式更好
    def test02():
        print("静态方法测试test02")
    
    # 静态方法,被调用的方法不可传self,和类化方法没什么不同,除了执行时的内存加载
    func3 = staticmethod(test02);
    
    # 方法变为类化或静态也可以使用注解
    @classmethod
    def test03(self):
        print("test03")
    
    @staticmethod
    def test04():
        print("静态方法测试test04")
        
    @property
    def test05(self):
        print("test05")
        return test10


if __name__ == "__main__":
    O1 = TestClass();
    O2 = TestClass();
    # 当对象已经定义了之后,可以直接在对象上添加任何想要的属�?,跟js的Object�?�?
    O1.FSDFDS = "fdsfgd";
    O1.str1 = "trest1";
    print(O1.str1)  # trest1
    O2.str1 = "gfdgfdg";
    print(O2.str1)  # gfdgfdg
#     print(O2.FSDFDS) # 错误,会抛异常
    print(TestClass.str1)  # 里面的
    TestClass.func1();  # 类名直接调用方法
    TestClass.func2();
    TestClass.func3();
    TestClass.test04();
    O1.__str__()
    TestClass.test02()
    print(TestClass.num1)  # 6666666666
    TestClass.num1 = 77777777
    print(TestClass.str3)
    print(O1.num1)  # 77777777
    O1.num1 = 8888888
    print(O2.num1)  # 77777777
    print(isinstance(O1, TestClass))
    O1();
#     print(TestClass.__username) # 抛异常,无法访问
#     print(O1.__username)    # 抛异常,无法访问
#     print(O1.getUsername())     # 可访问

    
def test10():
    print("test10")


O3 = TestClass()
print(O3.getUsername())  # 可访问
print(O3._TestClass__username)  # 可访问
print(O3.test05)
print(TestClass.func1())
print(O3.test05)
try:
    print(O3.test05())  # 错误,抛异常,O3.test05会返回一个None类型,后面加了()表示调用None(),但无法调用
    print(O3.test1)
except Exception:
    print("报错", Exception.args)
