# 使用requests进行网络爬虫,需要先安装模块

import requests
from urllib import request
from bs4 import BeautifulSoup

url = "https://www.ituba.cc/"
resp = requests.get(url) # 结果数据
# html = BeautifulSoup(resp.text,"lxml") # 需要使用lxml模块来解析爬取到的网页数据
html = BeautifulSoup(resp.text,"html.parser")
imgs = html.find_all("img")
for item in imgs:
    print(item.get("src"))
    request.urlretrieve("https:"+item.get("src"), item.get("src")[item.get("src").rfind("/")+1:]) # 将图片下载到本地
