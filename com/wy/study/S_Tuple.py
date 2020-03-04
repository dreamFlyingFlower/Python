# 可将元组的元素赋值给等同数量的变量,若不等同,会报错
str1, str2, str3 = ("434", "rer", "rerte");
print(str1, str2, str3)
print(__name__)
arr = ("fdsfd", "2343", 324);
print(arr[1])
# print(arr[9]) # 元组越界,抛异常
# in可以用来判断元组中是否存在某一个值,list也可以这样判断
print(324 in arr);
# 列表和元组互相转换
listq = list(arr);
print(listq)
arr1 = tuple(listq)
print(arr1)
tuple1 = ("fdwer", "rewrew")
print(34 in tuple1)  # 不抛异常,返回False
print(34 not in tuple1)
print(tuple("w32wfregfd"))
a, b = [1, 23, 6], [24, 56, 77]
print(zip(a, b))
print(list(zip(a, b)))
print(tuple(zip(a, b)))
print(tuple(zip(a, b))[0][0])


