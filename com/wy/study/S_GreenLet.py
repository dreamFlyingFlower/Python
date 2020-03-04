'''
协程,微程:比线程更小的处理程序,单个线程可支持上万的并发,且比线程消耗小
协程类似yield,当停留在yield时,出去时候是怎么样,再次调用yield还是怎么样
'''
from greenlet import  greenlet# 已经实现好的协程处理模块,需要安装
def test1():
    print(12)
    gr2.switch()    # 切换到test2方法开始调用,test1的线程阻塞在这里
    print(34)
    gr2.switch()
def test2():
    print(56)
    gr1.switch()
    print(78)

gr1 = greenlet(test1) #启动一个协程,但是并没有开始调用test1方法
gr2 = greenlet(test2)
gr1.switch() # test1方法才开始调用