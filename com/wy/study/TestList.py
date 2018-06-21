'''
Created on 2018年6月17日
@author: wanyang
    append和extend方法的不同,都是往list中添加元素,append是是什么就添加什么,extends必须是一个可迭代的变量,
        或者是一个单独的值,若是另外一个list,则会将list中的所有元素取出单个的添加到原list中,而append则是将另外的
        list当作原list的一个值整体添加到原list中
    +:将2个list相加会返回一个新的list,新的list就是2个list中的所有元素的集合,注意是返回新list
    del,remove:del是根据下标删除,remove是直接通过元素删除,而且只删除第一个
'''

list1 = [1,23,5,6,"fdgfe","gery","rewtre"];
#跟tuple和str一样的切片功能,不会存在数组下表越界的异常
print(list1[1:3]);
print(list1[1:6:2])
#可以利用这个特性删除list中的元素
#此种方法也不会存在检查list长度异常的问题
list1[1:3]=[]
print(list1)
#删除某个指定下标的元素
del(list1[1])
print(list1)
