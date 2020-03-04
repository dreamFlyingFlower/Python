'''
队列:queue:先进先出
lifoqueue:先进后出
priorityqueue:存储数据时可以设置优先级的队列
'''
import queue
queue1 = queue.Queue()
queue1.put(4)
print(queue1.get())
lifo = queue.LifoQueue()
lifo.put(1)
print(lifo.get())
priority=queue.PriorityQueue()
priority.put(3)
print(priority.get())