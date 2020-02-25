'''
@author: ParadiseWY

    collections模块,内置对一些基础类型的操作
    collections.defaultdict:默认字典,传入某个固定类型,则默认字典内所有的value默认都是该类型
    collections.namedtuple:可命名元组,即生成类似map类型的数据字典,但是key是隐藏的,不仅可以通过
        下标来查找元组中的数据,还可以通过key来查找数据
'''
import collections

defaultMap = collections.defaultdict(list);
defaultMap["le"].append("test");
print(defaultMap)
# 第一个参数是可命名元组的名字,�?要和变量名相�?,后面的是隐藏的key,可以通过.来调�?
nameTuple = collections.namedtuple("nameTuple", ["a", "b"])
# 申明�?个可命名元组,�?要重新定义变量来接受参数
ex = nameTuple("fdsfd", "fdsewr");
print(ex.a);print(ex.b);
