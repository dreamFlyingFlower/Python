# 测试常用类型
import time
import copy
a = True
print(int(a))  # 1
print(float(a))  # 1.0
b = False
print(int(b))  # 0
print(float(b))  # 0.0
c = 23.755678
print(round(c))  # 24,小数位默认为0,四舍五入
print(round(c, 3))
print(round(c, 4))
# 时间类型,需要引入时间类
print(time.time())  # 该方法返回的单位是秒,小数点后面是微秒
d = -400000000000000000
e = -400000000000000000
print(d == e)  # True,python中无论数据多大,只要字面量相同,那么==和is比较都是True
print(d is e)  # True
print(id(d))  # d和地址和e地址一样
print(id(e))
f = 'efr'
g = 'efr'
print(f == g)  # True
print(f is g)  # True
print(chr(64))  # 转为unicode,返回一个特殊字符
"""
 数字转字符串,若数字本身是整数,转字符串之后不带小数点
若数字本身是小数,结尾是0,若小数点之后只有1个0,则转成字符串之后0仍带上,若小数位大于1位,则将最后一个0去掉转成字符串
 科学计数法以小数的处理方法处理,若是完全转成数字之后编程整数,仍然带小数点以及1个0
"""
print(str(3)) 
print(str(3.5000))
print(str(23.455))
print(str(2.44e2))

list1 = [234,65756,['fdfgdg','fdsfwrw32']]
list2 = copy.copy(list1)
list2[2][0]="fdfrere"
print(list1)
print(list2)
list3 = copy.deepcopy(list1)
list3[2][0]=("tgtgte")
print(list1)
print(list3)