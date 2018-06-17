'''
Created on 2018年5月27日
@author: wanyang

    文件的读写:file=open(filename,mode):mode表示读写模式字符串
    r:只读,r+读写,追加,w覆盖写,w+读写(有问题,不要用),a:追加写入,a+读写,b打开二进制文件,U支持所有换行符
    以w的形式打开,若文件不存在,则会自动创建
    写入中文会乱码,怎么搞网上找
    使用with也可以打开文件,并且不用关心忘记关掉文件流
    文件的seek和tell方法,都是以字节为单位来操作指针,但是read和write方法都是以字符来读写数据
    FIXME
'''
write1=open("testFile.txt","w",encoding="utf8");
write1.write("gfdgfdgf");
write1.close();
read1 = open("testFile.txt", 'r');
print(read1.read());
read1.readline();
read1.close();

with open("testFile.txt", 'r') as f:
    print("do something")