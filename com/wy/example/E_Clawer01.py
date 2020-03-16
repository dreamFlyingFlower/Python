# 利用gevent进行爬虫,python3.8没有匹配的gevent,需要等待
from urllib import request  # 使用gevent爬虫,自动,gevent需要安装
import gevent, time
from gevent import monkey
from http.cookiejar import CookieJar
from bs4 import BeautifulSoup
monkey.patch_all()  # 把当前程序的所有的io操作给我单独的做上标记,必须要加,因为gevent不能urllib中的io操作


def f(url):
    resp = request.urlopen(url)  # 打开一个网页
    data = resp.read()  # 读取网页中所有的内容
    print('%d bytes received from %s.' % (len(data), url))


urls = ['https://www.python.org/', 'https://www.yahoo.com/', 'https://github.com/' ]
time_start = time.time()
for url in urls:  # 同步进行爬虫操作
    f(url)
print("同步cost", time.time() - time_start)
async_time_start = time.time()
gevent.joinall([gevent.spawn(f, urls[0]), gevent.spawn(f, urls[1]), gevent.spawn(f, urls[2]), ])  # 异步进行爬虫操作
print("异步cost", time.time() - async_time_start)
request.urlretrieve("http地址", "存储到本地的完整地址")  # 将文件直接下载到本地

# 爬虫的一种方法,不直接用request,而是伪造一个Request请求,加上一些请求头等
fake1 = request.Request("url")
fake1.add_header("user_agent", "Mozilla/5.0") # 添加浏览器类型
resp1 = request.urlopen(fake1)
print(resp1.read())

# 爬虫的另外一种方法,添加特殊处理方式
# 1.需要添加cookie的:HTTPCookieProcessor
# 2.需要代理才能访问的:ProxyHandler
# 3.需要https加密访问的:HTTPSHandler
# 4.有自动跳转的:HTTPRedirectHandler
# specialHandler = request.build_opener(HTTPSHandler())
# request.install_opener(specialHandler)
# request.urlopen("url")
cookie = CookieJar()
fake2 = request.build_opener(request.HTTPCookieProcessor(cookie))
request.install_opener(fake2)
resp2 = request.urlopen("url")
print(resp2.read())

# BeautifulSoup:解析html页面,需要安装beautifulsoup4,还需要安装lxml
soup= BeautifulSoup("html字符串","html.parser:指定解析器,html就是html.parser","from_encoding=utf8")

