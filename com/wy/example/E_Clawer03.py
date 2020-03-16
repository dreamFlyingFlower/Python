# 代理爬取网页
from urllib import request
# 国内ip代理网站:https://www.xicidaili.com/nt/
proxyHandler=request.ProxyHandler({"http":"112.95.205.29:8888"})
opener = request.build_opener(proxyHandler)
request.install_opener(opener)
resp = request.urlopen("http://www.baidu.com")
print(resp.read())
