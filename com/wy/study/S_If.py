if not "":
    print(11)
if not {}:
    print(22)
if not tuple():
    print(33)
if not []:
    print(44)
if not None:
    print(55)
if not dict():
    print(66)
if not 0.0:
    print(77)
if not range(0):
    print(88)
if " ": print(99)
elif 1: print(100)
else:print(101)
    
a=10
print(222 if a>10 else 333)
# a>10 ? print(11) : print(22) # 无该语法糖

# 以长度最短的为for循环的最大次数,每次都取相同下标位置的数据
tuple1 = (1,23,4,6,7)
tuple2=(12,5,7,8)
for k1,k2 in zip(tuple1,tuple2):
    print(str.format("{0}-{1}",k1,k2))

