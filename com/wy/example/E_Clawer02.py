# 随机获取请求头,通过403禁止访问的网页
from urllib import request
import random
headers = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3100.0 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Mobile Safari/537.36"
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:56.0) Gecko/20100101 Firefox/56.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0.1 Safari/604.3.5",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36 Request Payload",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:56.0)",
    "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11"
]
def getContent(url):
    """
    获取403禁止访问的网页
    """
    randomHeader = random.choice(headers)
    req = request.Request(url)
    req.add_header("User-Agent", randomHeader)
    req.add_header("Host","blog.csdn.net")
    req.add_header("Referer", "http://blog.csdn.net/")
    req.add_header("GET", url)
    request.build_opener(req)
    content = request.urlopen(req).read()
    return content
