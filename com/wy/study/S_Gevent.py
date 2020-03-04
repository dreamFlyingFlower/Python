'''
利用协程来进行io操作的自动转换,当发现io操作阻塞时,会自动转换到其他不需要io操作的线程上
利用了greenlet的协程操作,同时对其进行了封装
'''
from urllib import request # 使用gevent爬虫,自动,gevent需要安装
import gevent,time
from gevent import monkey
monkey.patch_all() #把当前程序的所有的io操作给我单独的做上标记,必须要加,因为gevent不能urllib中的io操作
def f(url):
    resp = request.urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))

urls = ['https://www.python.org/', 'https://www.yahoo.com/','https://github.com/' ]
time_start = time.time()
for url in urls: # 同步进行爬虫操作
    f(url)
print("同步cost",time.time() - time_start)
async_time_start = time.time()
gevent.joinall([gevent.spawn(f, urls[0]), gevent.spawn(f, urls[1]),gevent.spawn(f, urls[2]),]) # 异步进行爬虫操作
print("异步cost",time.time() - async_time_start)