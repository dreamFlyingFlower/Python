# numpy是python科学计算的基础包,存储其中的数据类型必须相同
# 切片功能和元组一样
import numpy
from numpy.core._multiarray_umath import arange

a = arange(5)
print(a) # 一个数组,类似list
print(a.shape) # a的长度
print(a.dtype) # a数组中元素的类型
a1 = numpy.array([numpy.arange(3),numpy.arange(5)]) # 生成一个长度为2,每行元素为array的二维数组
print(a1.shape)
print(a1[0][1]) # 等同于a1[0,1]
a2 = a.astype(numpy.float) # 将一个一维数组强行转换为其他类型,该类型为numpy自带类型,非python类型,只能转换一维数组
print(a2)
