'''
Created on 2020年2月25日

@author: wanyang

文件的读写:file=open(filename,mode):mode表示读写模式
    r:只读,r+读写,追加
    w覆盖写,w+读写(有问题,不要用)
    a:追加写入,a+读写
    b:打开二进制文件,U支持�?有换行符
    以w的形式打开文件,若文件不存在,则会自动创建,写入中文需要指定字符编码
    with也可以打开文件,并且不用关心忘记关掉文件,会自动关闭文件
    文件的seek和tell方法,都是以字节为单位来操作指针,但是read和write方法都是以字符来读写数据
'''

# file1 = open("testFile.txt", "w", encoding="utf8");
# file1.write("gfdgfdgf");
# file1.write("呵呵")
# file1.close();
read1 = open("testFile.txt", 'r',encoding="utf8");  # 可链式调用open("file").read()
# print(read1.read());    # 读所有
print(read1.readlines())    # 读所有,将每行内容加上换行符读取到一个list中
print(read1.readline());   # 读一行,空,因为指针已经到结尾了
read1.close();
print("___________")
read2 = open("testFile.txt", 'r',encoding="utf8");  # 可链式调用open("file").read()
for l in read2:
    print(l)
read2.close();

with open("testFile.txt", 'r',encoding="utf8") as f:
    print("do something")
    print(f.read())
