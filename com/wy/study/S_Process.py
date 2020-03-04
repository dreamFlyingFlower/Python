'''
进程操作:和线程操作是一样的,至不过在内存中不一样
'''
import multiprocessing
from multiprocessing import Process
def fn1(n):
    print(n)

if __name__ == "__main__":
    p1 = Process(target=fn1,args=(3,))  # 单进程
    p2 = multiprocessing.Process(target=fn1,args=(4,)) # 多进程
    p1.start()
    p2.start()