list1 = [1, 23, 5, 6, "fdgfe", "gery", "rewtre"]
for item in list1:
    print(item)
# 跟tuple和str一样的切片功能,不会存在数组下表越界的异常
print(list1[1:3])
print(list1[1:6:2])
list.insert(list1, 3, "32")
print(list1)
# 可以利用这个特性删除list中的元素
# 此种方法也不会存在检查list长度异常的问题
list1[1:3] = []
print(list1)
# 删除某个指定下标的元素
del (list1[1])
print(list1)
print(range(-1, 10))
for item in range(-1, 10, 2):
    print(item)
print([item * 2 for item in range(5) if item % 4 == 0])
a = (12, 45, 76, "hg")
print(id(a))
a *= 3
print(a)
print(id(a))
list2 = [23, 54, 77, 88, 99.9, 100.01]
del list2[-1]
print(list2)
print(list2[1])
# print(list2.index(99))    # 抛异常
print(list2.index(23))
# 切片方法,同字符串
print(list2[::])
# list2.sort(reverse=True)
list.sort(list2, reverse=True)
print(list2)
print(max(list2))
print(sum(list2))
list3 = ["fwewr", "ewrew", "ew4rew"]
list.sort(list3)
print(list3)
enum1 = enumerate(list3)
print(enum1)
# print(list(enum1))    # 将enumerate转换为list或tuple之后,enumerate中就空了,不可进行二次转换,和generator一样
for index,item in enum1:
    print(index,item)

