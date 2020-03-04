'''
Created on 2020年2月28日

@author: wanyang
'''
import random

print(random.random()) #[0,1)
print(random.uniform(1,10)) #在random基础上指定了区间,返回的是1,到10之间的小数,不包括10
print(random.randint(1,10)) #[1,10]
print(random.randrange(1,10))   #[1,10)
print(random.choice("fdsfewrew")) # 随机从序列,可迭代列表中获得一个元素
print(random.sample("fdsfewrew",3)) # 随机从序列,可迭代列表中获得指定个数的元素,并返回一个列表