'''
多线程,python的多线程不管cpu有多少核,同时间只有1个线程在执行,这是python的缺陷
'''
import threading


# 直接使用threading来启动线程
def fn1(arg1, arg2):
    lock.acquire() # 加锁
    print("fdsewrew", arg1, arg2)
    lock.release() # 释放锁
    semaphore.acquire() # 加上信号量锁
    print("fere")
    semaphore.release() # 解开信号量锁

lock = threading.Lock() # python的锁
semaphore = threading.BoundedSemaphore(5)   # 信号量,表示同时最多有几个小城同时运行
t1 = threading.Thread(target=fn1, args=(12, 44))
t1.start()


# 通过继承的方法使用线程,需要重写run 方法
class TestThread(threading.Thread):

    def __init__(self):
        # 2种方式的调用超类都可以
        super(TestThread, self).__init__()
        super().__init__()

    def run(self):
        print("terewrew", threading.current_thread(), threading.active_count())


t2 = TestThread()
t3 = TestThread();
t2.setDaemon(True)  # 设置为守护进程,当主线程执行完毕之后,不管其他线程是否执行完毕,直接结束程序
t2.start()
t3.start()
t2.join()  # 等待t2线程指定完毕之后才继续走主线程
