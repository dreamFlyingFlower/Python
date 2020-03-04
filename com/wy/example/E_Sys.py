"""
系统模块:获得系统信息,模块的导入默认先从当前目录开始查找,之后从lib以及site-packages等第3方库查找
若是自己写了一个库,可以直接放到site-packages目录下
"""
import sys

# 输出python的环境变量,有多个,有标准库(lib),第3方库(site-packages)
print(sys.path)
"""
 输出执行当前python脚本的路径以及参数列表,路径是相对于python执行时的路径,ide就是执行绝对路径,故输出绝对路径
 若是在控制台用python命令执行脚本,那么控制输入的执行脚本路径就是第1个参数的值
 如python com/wy/example/E_Sys.py,则sys.argv[0]输出为python com/wy/example/E_Sys.py
 sys.argv->list,list[0]是执行文件时的相对路径,依次是执行文件时的参数
"""
print(sys.argv)  # ['F:\\repository\\Python\\Python\\com\\wy\\example\\E_Sys.py'],是一个列表,主要是获得执行参数
print(sys.argv[0])  # F:\\repository\\Python\\Python\\com\\wy\\example\\E_Sys.py
sys.stdout.write("text")    # 标准输出
sys.stdout.flush()  # 将内存中的数据刷新到标准输出上
print(sys.getdefaultencoding()) # 获得当前文件默认编码

import os

# 直接执行系统命令,输出到屏幕上,无法赋值给变量,即使赋值给某个变量,输出变量也是0
t1 = os.system("dir")
print(t1)  # 0
t2 = os.popen("dir").read() # 若不使用read,会保存到t2中,但是输出的是内存地址,加上read则可以输出结果
print(t2)
print(os.path.abspath(__file__))    # 获得当前文件的绝对路径
print(os.path.dirname(os.path.abspath(__file__)))   # 返回当前文件的绝对路径的父级文件夹绝对地址
t3 = os.walk("F:\\repository\\BMS\\static\\") # 获得当前目录下的所有文件,返回一个generator
    
print(os.getcwd())
print(os.curdir)
print(os.pardir)