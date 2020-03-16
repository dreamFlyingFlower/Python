# 使用python打开一个网页
import webbrowser
import os
# 直接打开一个新的网页
webbrowser.open_new_tab("https://www.baidu.com")
# 在windows系统控制台中运行命令,关闭浏览器
os.system("taskkill /F /IM chrome.exe")