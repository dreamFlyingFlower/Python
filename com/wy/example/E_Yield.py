'''
Created on 2020年2月27日

@author: wanyang

利用yield实现双线并行,类似线程,
'''
import time

def consumer(name):
    print("%s 准备吃包子啦!" % name)
    while True:
        baozi = yield   # 接收来自send方法的通知和参数
        print("包子[%s]来了,被[%s]吃了!" % (baozi, name))

c = consumer("客户")
c.__next__()

# b1= "韭菜馅"
# c.send(b1)
# c.__next__()

def producer(name):
    print(name)
    c = consumer('A')   # 必须i先调用一次,此时并不是执行consumer,而是生成了一个生成器
    c2 = consumer('B')
    c.__next__()
    c2.__next__()
    print("老子开始准备做包子啦!")
    for i in range(10):
        time.sleep(1)
        print("做了1个包子,分两半!")
        c.send(i)   # send方法通知yield再次运行,并传递参数给yield
        c2.send(i)

producer("包包子的")
