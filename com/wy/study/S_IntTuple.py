# 继承系统的元组,并派生自定义的元组
class IntTuple(tuple):

    def __new__(self, iterable):
        res = (x for x in iterable if isinstance(x, int) and x > 0)
        return super(IntTuple, self).__new__(self, res)
    
    def __init__(self, iterable):
        super(IntTuple, self).__init__()
        print(iterable)  # [1, 3, 5, -4, '54e5']


t = IntTuple([1, 3, 5, -4, "54e5"]);
print(t)  # (1, 3, 5)
