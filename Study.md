# Python

## 一.简介

1. 本基本的python版本为3.8.1,所有的实力都是在该版本基础上所测试
2. python是弱语言,是解释执行,类似javascript,一个python文件叫做一个module
3. 在3以后的版本中,long类型已经取消了,只有int,而int可以存任意整数类型的值
4. 在3.8版本中,整数类型用==和is比较的结果相同,他们的id是相同,不论整数的值是多少
5. python2的默认编码是ASCII,不支持中文,需要显示的指定,而python3的默认编码是[unicode](https://www.cnblogs.com/crazylqy/p/10184291.html),可以很好的支持中文以及其他类型字符,但为了兼容2和3版本,最好都在文件的开头指定字符集编码:\# -*- coding:utf-8 -*-
6. scrapy:创建写爬虫的文件
7. 判断数据类型可以使用type,如type(tuple) is tuple,返回True表示是元组类型
8. 



## 二.基础知识

### 1.数据类型

#### 1.1 基本数据类型

1. 常量:python实际上没有常量,只是约定俗成的标识都大写的变量为常量,实际上仍然可以修改
2. 字符串(str):
   1. 单双引号可以创建字符串
   2. 字符串不可变,也不支持单字符串类型
   3. 默认是unicode的utf8编码,也就是16位的2进制编码
   4. 3个单引号或3个双引号之间的内容可以换行,输出时自带换行符
   5. 将多个字符串放在一起,默认就是拼接,如"ssss""fdfd"->"ssssfdfd"
3. 整数(int):
   1. 在python2中为4个字节,但在python3中已经可以存储任意大小的数字而不会造成溢出
   2. 0b或0B:开头是零,将10进制数据用二进制表示
   3. 0o或0O:开头是零,结尾是欧,将10进制数据用八进制表示
   4. 0x或0X:开头是零,将10进制数据用16进制表示
4. 长整数(long):,在python3中已经没有long类型了,都是int类型
5. 单精度浮点型(float):单精度浮点数
7. 布尔(boolean):True/False,可以与数字做运算,此时true为1,false为0
8. range(m[,n,step]):range列表,创建整数列表,默认从0开始创建,若传n,则是从m开始一直到n,不包含n,step为步长,表示每次增加或减少的数字
9. zip:zip(list1,list2...listn):将多个列表合成转化成一个元组,并返回一个zip对象,若需要使用zip对象,需要先转化为元组或列表,如tuple(zip)->得到一个2纬元组,list(zip)->得到一个元组列表
10. complex:复数,复数由实数和虚数组成,一般形式为x+yj,x是复数的实数部分,y是复数的虚数部分,x,y都是实数



#### 1.2 数据结构类型

##### 1.2.1 列表(list)

> 内置可变序列,包含多个元素的有序连续内存空间

1. 元素可以是任意类型,且长度可变,是一种可迭代类型,如m=[123,45,66,77,"342"]

2. 字符串和列表有很多相似之处,大部分字符串中可用的方法都可用于列表,比如切面

3. 列表可以接受元组,字符串,其他序列类型(range),可迭代类型生成列表

4. 列表创建方式
   1. m=[12,22]
   2. m=list()或m=list(range(15))或m=list("fdsewrewrew"),将字符串拆分为单个字符存储的列表
   3. m=[for item in range(5)]->[0,1,2,3,4]
   4. m=[item*2 for item in range(5)]->[0,2,4,6,8]*
   5. 列表生成器:m=[v*2 for vin range(5) if v%4 == 0]->[0,8],顺序对条件进行过滤,最后将值赋给v,for循环可以有一个,也可以有多个,根据情况进行赋值
   
   

##### 1.2.2 元组(tuple)

> 是不可变序列,不能修改元组中的任何数据,只能访问和删除,也没有增加,修改,删除元素的操作

1. 元素可以是任意类型,也是一种可迭代类型,如m=(1,2)
2. 元组中的方法和列表基本相同,可以索引访问,切片,连接操作,比较运算
3. 元组可以接受列表,字符串,其他序列类型(range),可迭代类型生成元组
4. 创建方式
   1. 括号创建,如:m=(1,2),若是只有一个元素,逗号必须有,括号也可省略,但为了可读性,不要省略
   2. 对象创建,如:m=tuple(),创建了一个空的元组
   3. 列表创建,如:m=tuple([12,34,"fd"])
   4. range创建:如:m=tuple(range(10))
   5. 字符串创建:如:m=tuple("fdfdwerw")



##### 1.2.3 生成器推导式(generator)

> 和列表生成器一样,只是用()包裹其中的代码,生成器生成的既不是列表也不是元组,而是一个对象.可以通过元组和list对生成器进行转换
>
> m=(x*2 for x in range(10) if x%4==0)->根据表达式依次调用条件接口,最后将值赋给x,最终生成m

1. tuple(m)或者list(m)之后,m中将不再有元素,是一个空的对象,再次使用tuple或list将得到一个空的对象
2. 可调用next(m)查看m中元素,和java中的迭代器一样,但是在没有更多元素的时候调用next方法,会抛异常
3. 查看一次之后m中的该元素将无法被再次方法,若想要再次访问生成器中的元素,需要重新生成
4. for循环可以有多个,根据情况而定



##### 1.2.4 字典(dict)

> 字典是无序的键值对可变序列,类似java中的map,整数,浮点数,字符串,元组可作为key,任意类型可作为value

1. 字典创建

   > m={a:b,c:d},和对象的创建一样
   >
   > m=dict(key1=value1,key2=value2)
   >
   > m=dict([(key1,value1),(key2,value2)])
   >
   > list1=[],list2=[],m=dict(zip(list1,list2)):list1的长度必须比list2的长度大
   >
   > m=dict.fromkeys([]):将一个列表转化成一个只有key的字典,key的值都为None

2. 字典推导式:{key1:value1 for  item1 in  可迭代对象  for item2 in 可迭代对象 if  cnd1}.其中的for循环可以只有一个,也可以有多个.key1可以是item1处理后的对象和value1可以是item2处理后的对象,可根据需求处理

3. 字典在内存中开销巨大,典型的空间换时间

4. 键查询速度很快

5. 往字典里新增时候可能会导致扩容,会导致键的次序改变,所以不要在遍历的同时修改字典

6. 在遍历字典时,默认是直接遍历key,也可以同时遍历key和value,如for k,v in dict.items()



##### 1.2.5 集合

1. 集合是无序列表,元素不能重复,集合底层是字典实现,集合的所有元素都是字典中的key

2. 创建集合

   > m={1,23,56}
   >
   > m=set(tuple),只能将tuple和list转换为set,set中不能直接构造值
   >
   > m=set(list)

3. 集合推导式:{ele for key in 可迭代对象 可添加if等条件},for循环可有多个,ele是key进行处理后的对象

4. 集合的并集,交集,差集等,原集合不会改变,只会生成新的集合

   > m|n或m.union(n):取m和n并集,重复元素只取一次
   >
   > m&n或m.intersection(n):取m,n的交集,重复元素只取一次
   >
   > m-n或m.difference(n):取差集,即m中,n中没有的元素
   >
   > m.issubset(n):m是否是n的子集,返回True/False

5. 







### 2 逻辑运算符

1. or:或运算,和java中的||一样,会有短路
2. and:和运算,和java中&&一样
3. not:非,和!一样
4. ==:相同,类似java中的equals,默认会调用对象的\_\_eq()\_\_方法.不同版本对==的解析不一样
   1. 当比较的是数字时,不管数字大小,得到的结果都是True
   2. 当比较的是字符串时,不管字符串中有什么特殊字符,得到的结果都是True
   3. 其他类型需要看情况
5. is:判断两个标识符是不是引用同一个对象,即比较id的值,类似java中的==.不同版本对数字的==和is解析不同
   1. 当比较的是数字时,不管数字大小,得到的结果都是True
   2. 当比较的是字符串时,不管字符串中有什么特殊字符,得到的结果都是True
   3. 其他类型需要看情况
6. is not:is的相反函数



### 3 序列解包

1. 序列解包用于元组,列表,字典,可以更方便的对多个变量赋值

2. 元素:m,n=(10,20)->m=10,n=20或(m,n)=(10,20)->m=10,n=20

3. 列表:[m,n]=[10,20]->m=10,n=20

4. 序列解包时默认是对键进行操作,如果需要对键值进行操作,则需要用items,对值解包则需要用values

   > m={key1:value1,key2:value2,key3:value3}
   >
   > 默认或键解包:a,b,c=m->a=key1,b=key2,c=key3
   >
   > 键值对解包:a,b,c=m.items()->a=(key1,value1)
   >
   > 值解包:a,b,c=m.values()->a=value1



## 三.常用内置函数

### 1.通用函数

1. id(obj):获得对象在内存中的地址值

2. type(obj):获得对象的类型

3. del obj:删除对象,该方法可删除元组,列表,字典中指定元素

   > 删除元组元素:del tuple[1]或del(tuple[1])
   >
   > 删除列表元素:del list[1]或del(list[1])
   >
   > 删除字典元素:del dict[key]或del(dict[key])

4. dir(m):获得m所有的属性,方法

5. m.__dict\_\_:对象实例的属性字典

6. isinstance(m,class):判断m实例是否为指定的class或class的子类,class直接是类名即可,不需要带__class\_\_

7. help(m):获得m可以使用的方法

8. print(x,end=""):print默认换行,若想修改换行符,可使用end参数指定输出的结尾标识符

9. m+n:
   1. 若m,n都是字符串,则拼接
   2. 若m,n都是数字,则做加法运算
   3. 若是m,n类型不同,抛异常
   4. 若m,n都是元组,则会将m,n中的元素合成一个新的元组返回
   5. 若m,n都是列表,同样会将2个列表中的元素合称一个新的列表返回

10. m*n:

   11. 此处n为正整数,若m为字符串,则直接复制n次m拼接起来

   12. 若m是数字,则做乘法运算

   13. 若m为list,则将list中的元素复制n次拼接成一个新的list列表

   4. 若m为元组,则同样将元素的元素复制n次之后形成一个新的元组

11. m=input("提示语"):获得从控制台输入的值,并将其赋值给m,不管输入的什么类型,m都是字符串类型

12. len(m):返回字符串,元组,list,dict的长度

13. m in n,m not in n或not m in n:判断m是否存在于n中
    1. 当m,n为字符串时,判断n中是否存在m,且m,n都必须是字符串,否则抛异常
    2. 当n为元组时,m可为任意类型,不会抛异常
    3. 当n为字典师,检查字典的key中是否有m键
    4. 当n为list时,检查n中是否有m

14. range(m,n,step):创建整数列表,从m到n,不含n

15. sorted(iterable[,reverse=]):给迭代对象排序,默认升序,返回一个新的列表,reverse=True时降序

16. reversed(iterable):对迭代对象进行逆序排列,不修改原对象,返回一个新的对象,和list,tuple的reverse方法不同

17. max(iterable):获得任何迭代对象中最大的值

18. min(iterable):获得迭代对象中最小的值,非数字忽略

19. sum(iterable):获得迭代对象中数值的总和,非数值忽略

20. locals():直接调用,返回最近的作用域中的本地变量,以字典形式输出

25. globals():直接调用,返回当前module中的全局变量,以字典形式输出

26. class.mro():查看类的继承结构层次



### 2.字符串

1. len(m):拿到m长度,是字符串长度,而非字节长度

2. ord(m):将单字符串转换为对应的unicode编码

3. str(m):将其他类型转为字符串
   1. 当m=100->"100"
   
   2. 当m=1.0->"1.0"
   
   3. 当m=2.500->"2.5"
   
   4. 当转换科学计数法的时,m=1.44e2->"144.0"
   
   5. 当m=1.4433e2->"144.33"
   
      > 由此得出规律:当m为整数时,转成字符串仍为整数
      >
      > 当m小数时,转成之后必须带小数.
      >
      > 若小数位的第1位就是0,而且只有这一个小数,那么0保留
      >
      > 若小数的最后一位是0或连着几个都是0,而小数位的第1位非0,那么0全部去掉
      >
      > 科学计数法转换为小数转换,转换规则同小数
   
4. m[n]:从字符串m中获取指定下标n处的字符
   1. m为任意长度字符串,n为整数
   2. 若从m开头提取,n从0下标开始计数;若从m末尾开始提取,则n从-1开始
   3. 若n超出了字符串的长度,则抛异常
   4. []只能用来获得字符串,但是不能修改指定下标的值,因为字符串不可变
   
5. m[a:z[:step]]:切片(slice),若m="qwertyuiop"

   1. 若z超出m的总长度,默认为m的长度下标

   2. 没有参数step,从字符串m的a下标开始到z结束截取字符串,含头不含尾

      > 如:m[1:6]="werty"

   3. 有参数step,则从a-z获得的结果中每隔step个值获得一个值拼接后返回.

      > 如:m[1:6:2]="wry"

   4. [:] :直接返回m,等同于[::1]

   5. [::-1] :相当于将m进行反转

      > 如:m[::-1]="poiuytrewq"

   6. [:z] :返回前z个字符串,不包含下标为z的字符,若z为负数,只是取开始下标的时候从字符串末尾开始计数,但仍然是向末尾截取字符串,而不是从末尾向开头截取字符串

   7. [a:] :返回从a下标开始的字符串,包含a下标字符,若a为负数,则从末尾开始计数,仍然向末尾截取

      > 如:m[-3:]="iop"

6. m.replace("n","x"):将m中的n字符串修改为x,得到一个新的字符串,m仍然不变

7. str.split(m[,n])或m.split([n]):将字符串m按照指定的字符串拆分,得到的是一个list

   1. 当n不存在,默认以空格,换行符,制表符拆分字符串
   2. 可以不指定n,但是n不可为"",会抛异常,但可以是" "

8. str.join(delimiter,iterable)或delimiter.join(iterable):将一个可迭代的对象(元组或list等)用delimiter拼接起来,delimiter只能是字符串,不可为""

9. str.startswith(m,n)或m.startswith(n):判断字符串m是否以n开头

10. str.endswith(m,n)或m.endswith(n):判断字符串m是否以n结尾

11. str.find(m,n[,index])或m.find(n[,index]):从字符串m中查找字符串n第一次出现的下标,m,n都必须是字符串,若n非字符串,会抛异常.若不指定index,则从下标0开始查找

12. str.rfind(m,n[,index])或m.rfind(n[,index]):查找n最后一次出现的位置,其他同find

13. str.count(m,n)或m.count(n):m,n都必须是字符串,从m中查找n出现的次数

14. str.isalnum(m)或m.isalnum():m是否全是数字或字母,包含汉字,不能带特殊字符

15. str.isalpha(m)或m.isalpha():m中是否全是字符,包含汉字,不包含数字,特殊字符

16. str.isdigit(m)或m.isdigit():是否是一个整数字符串,不能是小数

17. str.isspace(m)或m.isspace():m是否为空白字符串,""并不是空白字符串,只包含空格,制表符和换行才算,判断""只能通过len("") == 0

18. str.isupper(m)或m.isupper():m是否全部为大写字母

19. str.islower(m)或m.islower():m是否全部为小写字母

20. str.strip(m[,n])或m.strip([n]):去除m首尾的n字符串,n不传则默认去除空格,换行,制表符

21. str.lstrip(m[,n])或m.lstrip([n]):去除m左侧的n字符串,str.rstrip去除右侧的

22. str.capitalize(m)或m.capitalize():将整个字符串的首字母大写

23. str.title(m)或m.title():将m中每个单词的首字母大写,只要单字符之间不是用字符连接的都算一个单词

    > 如:fds_r3wefwfter43543h_htytr,title之后->Fds_R3Wefwfter43543H_Htytr

24. str.upper(m)或m.upper(),str.lower(m)或m.lower():将m中所有字符都大写或都小写

25. str.swapcase(m)或m.swapcase():将m中所有的字符大小写逆转,大写转小写,小写转大写

26. str.center(m,n,x)或m.center(n,x):将字符串m扩展到指定长度n,同时两边填充x单字符,x只能是一个字符,多于1个字符抛异常

    > 如:str.center("fdfd",11,"|")->||||fdfd|||

27. str.ljust(m,n,x)或m.ljust(n,x),str.rjust(m,n,x)或m.rjust(n,x):同center,只是m位置在左边或右边

28. str.format(m,p1,p2...pn)或m.format(p1,p2...pn):m为需要格式化的字符串,参数可以是任意类型.有2种形式

    1. m中占位符用参数索引表示,从0开始,参数索引可重复使用,只要参数索引下标对应占位符即可,同时参数的个数必须多于m中占位符个数,可多不可少,否则抛异常

       > str.format("惹我{0},范我惹我{1},{0}","好",23)->"惹我好,范我惹我23,好"
       >
       > str.format("%s,%s")->同{},只不过不能下标重用,必须一一对应

    2. 用参数名表示,参数的形式为key=value,参数位置随意,和用索引一样,在m中出现的占位符,在参数中必须存在,否则抛异常

       > str.format("范德{name},{tttt},{name},那么{beauty}",tttt="外人23",name="dfsfds",beauty="")

    3. 格式化:需要用冒号(:)来分隔参数

    4. 填充和对齐:^,<,>分别是居中,左对齐,右对齐,可以加上宽度.格式:索引或key:需要填充的单字符对齐参数,宽度,冒号是必须的,冒号后的参数是连接在一起的

       > str.format("我是{0},hi好{1:|^10}","秒","giao")->"我是秒,hi好|||giao|||"
       >
       > str.format("我{name},{tt:|^10}",name="方法",tt="MM")->"我方法,||||MM||||"

    5. 数字格式化

       1. {pn:4d}:数字格式化,默认中间对齐,pn位数不够用空格代替
       2. {pn:.2f}:保留2位小数,{:.0f}:不带小数
       3. {pn:,}:以逗号分隔的数字格式
       4. {pn:.2%}:百分比格式,数字表示百分比格式的小数位

29. io类,将字符串转为流数据来修改,需要到如io,import io

    1. m="qwertyuiop",n=io.StringIO(m)->得到m的字符流,此时n可变

    2. n.seek(x):将指针指向x下标的字符,从0开始,x可超出字符串的总长度,若超出,n的值仍然不会变,只是做了一个标记

    3. n.write(y):将2中所指向的下标x处的字符替换为y.y有多少个字符,就将从x处(包括x)开始替换多少个字符.若x超出了n的长度,中间空格填充,若y的长度超过n的剩余可替换长度,将会继续填充

       > n.seek(30)
       >
       > print(n.getvalue())  #仍然不变
       > print(len(n.getvalue())) #仍然不变
       >
       > n.write("23fdsfdsfdsfewrew43543534")
       > print(n.getvalue()) ->"qwertyuiop                    23fdsfdsfdsfewrew43543534"

    4. n.getValue():得到write之后的新值



### 3.数字(number)

1. /:python中是除法,但是得到的结果是浮点数类型,除数为0时抛异常
2. //:除法,得到的结果是整数类型,除数为0抛异常
3. %:模,取余
4. **:幂,如2\*\*3=8
5. divmod(m,n):同时得到m/n的商和余数,即同时得到//和%的结果
6. int(m):将其他类型转化为数字
   1. 纯数字组成的字符串可转,带其他字符串不可转
   2. boolean类型true转为1,false转为0
   3. 浮点数类型直接设置小数点后的值,不进行四舍五入
7. float(m):将其他类型转换为浮点数,条件等同int,但是boolean类型会转成1.0,0.0
8. round(m[,n]):m四舍五入,若n不存在,则只返回int部分,若n存在,则返回n位数的小数
9. chr(m):将65536之内的正整数转换为对应的单字符串



### 4.列表(list)

1. m+[n]:列表m的末尾添加一个n的元素,该方式不要用,太消耗内存,而且会返回一个新的list
2. list.append(m,n)或m.append(n):m列表中添加n元素到末尾,n可为任意元素,是什么就添加什么到m中
3. list.extend(m,n):将n列表中所有的元素添加到m列表末尾,n必须是一个可迭代的对象
4. list.insert(m,index,x):在m的index位置插入单个x元素,index从0开始,在index插入,而不是index+1插入
5. list.remove(m,n):删除在m中首次出现的n元素,是元素而非下标,若不存在n元素,抛异常
6. list.pop(m,[index]):从末尾删除并返回删除的元素,若指定index,则删除下标为index的元素
7. list.clear(m):清空m,此时m仍然存在,只不过长度为0
8. list.index(m,n[,b,e]):返回m中n元素首次出现的下标,若n不存在,抛异常.b为索引开始下标,e为索引结束下标
9. list.count(m,n):返回n在m中出现的次数
10. list.reverse(m):将列表反转
11. list.sort(m):列表排序,默认升序,list.sort(m,reverse=True):降序
12. del list[n]:删除list列表中下标为n的元素,若n超过list长度,抛异常
13. 切片方法,同字符串
14. zip(list1,list2...listn):将多个列表按照顺序合成一个元组,返回一个zip对象



### 5.元组(tuple)

1. 除了增加,修改,删除元素的方法没有之外,其他方法和列表差不多
2. m[index]:通过元组下标访问元组中的元素,下标超长将抛异常
3. m.index(n[,b,e]):返回m中n元素首次出现的下标,若n不存在,抛异常.b为索引开始下标,e为索引结束下标
4. m.count(n):返回n在m中出现的次数



### 6.字典(dict)

1. m.get(key[,default]):获得m中的key的值,若key不存在或key对应值为None,那么输出default的值
2. m[key]:通过key值来获得对应的value,若key不存在,抛异常
3. m[key]=value:往m中设置值
4. m.setdefault(key[,default]):往字典中设置键值对,若default不设置,则默认为None;
5. m.items():以元组的形式列出字典中的key-value键值对,类似java的entry
6. m.keys():列出字典中所有的键列表
7. m.values():列出字典中所有的值列表
8. m.update(n):n覆盖m中的字典元素以及值,将m,n各自没有的值合并
9. m.__delitem\_\_(key):删除m中的key,或者使用del m[key]
10. m.pop(key):根据key删除dict中的元素,返回被删除键值对的值,del和__delitem\_\_方法无返回值
11. m.popitem():随机删除m中的元素返回键值对元组,若m已经为空时,抛异常
12. m.clear():清空字典中的元素



### 7.集合(set)

1. m.add(n):往集合中添加元素
2. m.update(n):往m中添加多个元素,n是列表
3. m.remove(n):根据元素删除集合中的元素,若元素不存在,抛异常
4. m.discard(n):根据元素删除集合中的元素,若元素不存在,不会抛异常,无返回值
5. m.pop():随机删除m中一个元素,并返回这个元素
6. m.clear():清空集合中所有元素
7. m.union(n):取m,n的并集,重复只取一次,返回一个新的集合
8. m.intersection(n):取m,n的交集,重复元素只取一次,返回一个新的集合
9. m.difference(n):取差集,即m中有,n中没有的值,返回一个新的集合



### 8.枚举(enumerate)

1. 主要用于将可迭代列表,字符串或其他支持迭代对象组合成一个索引序列,同时列出数据下标和数据
2. enumerate(seq[,start]):seq可以是字符串,元组等可迭代对象,start指定转换后的枚举下标起始值,默认0开始

```
list1 = [12,545,767,99]
print(list(list1))	# [(0,12),(1,545),(2,767),(3,99)]
for index,item in enumerate(list1):
	print(index,item)	# index是下标,item是数据
```



## 四.控制语句

> 所有的控制语句条件语句并不是用括号()隔绝代码块,而是用空格和冒号

### 1.if

1. python中,False,0,0.0,None,空集合,空元组,空列表,空dict,空字符串,空range对象,空迭代都判断为False.字符串中全是空格,制表符,换行符的,判断为True,"False"是True,并不会强转

2. if cnd1:res1 else: res2或if cnd1:res1

   ```python
   if cnd1:
   	dosomething1
   else:
   	dosomething2
   以上模式若res1只有一行语句,可以直接接在:号写一行,如if cnd1:res1
   if cnd1:
   	dosomething1
   elif cnd2:
   	dosomething2
   else:
   	dosomething3
   ```

   

3. 一行if-else:条件为True的结果语句 if cnd1 else 条件为False的结果语句



### 2.while

### 3.for

#### 3.1 普通for循环

```python
for item in 可迭代对象:
	dosomething1
    contine(满足某种条件之后本关键字后面的代码将不再执行,直接执行下一次循环,适用于while)
    break(满足某种条件之后打断整个循环,后面的循环不再执行,同样适用于while)
tuple1,tuple2,tuple3
for key1,key2,key3 in zip(tuple1)
```

#### 3.2 zip循环

> zip循环可以将多个元组,列表同时进行循环,以长度最短的为最大循环次数.每次取相同下标的值

```
tuple1,tuple2,tuple3
for key1,key2,key3 in zip(tuple1,tuple2,tuple3):
	print("{0}-{1}-{2}".format(key1,key2,key3))
```



### 4.else

> 适用于while和for循环,若while和for循没有被break,那么在循环完成之后必然会执行else之中的语句

```
while cnd1:
	dosomething1
else:
	dosomething2
	
for item in tuple:
	dosomething1
else
	dosomething2
```



## 五.函数

### 1.简介

1. 函数就是代表一个任何或一个功能,实现代码的复用

2. 函数没有重载方法,一个module或class中不能有同名方法,即使参数不一样

3. 函数必须有函数体,若没有,编译不通过,实在没有,可以使用pass关键字作为函数体

4. 函数分为内置函数,即python环境自带;标准库,需要用import导入;第三方库,别人写的库;自己写的库

5. 函数定义:def:固定写法,表示这是一个函数,fn:方法名,见名知意,args:参数

   > def   fn(args):
   >
   > ​	''' 我是注释,写在里面可以调用help(fn\_\_doc\_\_)方法获得注释 '''
   >
   > ​	dosomething

6. 函数和其他基本类型,数据类型一样,都是对象,也可以用id,type等方法,如id(fn),只需要名字,不要带()

7. 函数不需要指定返回值类型,若需要返回值,可以使用return value

8. 若结尾有return语句,且函数能执行到该return,那么就可以返回值,若没有return,则返回None

9. 因为python是解释执行,所以必须先定义函数,之后才能调用

10. 内置函数对象会自动创建,第3方库在import时会执行def语句

11. 注释需要写在方面里面,调用help(fn\_\_doc\_\_)方法可以获得注释



### 2.参数

#### 2.1 基本类型参数

1. 不可变参数,如int,str,float,元组,boolean在传递时,形参和实参是同一个对象,但是给形参重新赋值时,由于形参是不可变类型,需要新建一个新的值赋给形参,故在函数内给形参重新赋值时,形参的id已经变了,已经不再给实参是同一个内存地址了.若是传递的可变参数,那么在修改形参时,也会同时修改实参
2. 形参不需要声明参数类型,若没有参数,括号也必须有
3. 括号内参数为多个时,用逗号隔开,每个形参可用key=value的形式指定默认值,默认值参数必须写在最后
4. 命名参数:即传递参数时使用key=value的形式传递参数,位置可以不定义,根据key的名称来传递参数
5. 当调用函数时,参数个数必须和参数列表对应,参数个数必须相等.若是函数给形参指定了默认值,那么调用方法时,该形参可以不传,此时实参个数小于行参个数
6. 



#### 2.2 可变参数

1. *param:将多个参数全部放到一个形参中,该形参的类型最终为元组

2. **param:将多个参数全部放到一个形参中,该形参的类型最终为dict

   ```
   def fn(a,b,*c):
   	print(a,b,c)
   fn(1,2,3,4)->1,2,(3,4)
   def fn1(a,b,**c):
   	print(a,b,c)
   fn1(1,3,key1=value1,key2=value2)->1,3,{key1:value1,key2:value2}
   def fn2(a,b,*c,**d):
   	print(a,b,c,d)
   fn2(1,2,3,4,5,key1=value1,key2=value2)->1,2,(3,4,5),{key1:value1,key2:value2}
   ```

   

3. 可变参数必须放在普通参数,默认参数之后,可变参数的元组参数必须放在字典参数前

4. 若在可变参数之后还要传参,该参数必须是强制命名参数,如key1=value2

5. 形参的顺序:普通参数,默认参数,元组参数,字典参数,如def fn(p1,p2,p3=value1,*p4,**p5)

6. 当函数定义了*arg了,而实参传入时多余参数也是元组,list等数据类型,在放入arg中仍以实参的形式,并不会进行相应的拆包

   ```
   fn(*params1,**params2):
   	print(params1,params2)
   fn((12,434,5),(34,76),["fds","ewr"])->params1:((12,434,5),(34,76),["fds","ewr"])
   ```

   



#### 2.3 浅拷贝和深拷贝

1. 浅:直接将源对象的子对象内存地址指向新对象,不管是源对象还是新对象的改变,都会同时改变另外一个对象.注意是对象里的子对象,对对象的表层地址仍然是不会影响的

   ```
   list1 = [234,65756,['fdfgdg','fdsfwrw32']]
   list2 = copy.copy(list1)
   list2[2][0]="fdfrere"
   print(list1)  # [234, 65756, ['fdfrere', 'fdsfwrw32']]
   print(list2)  # [234, 65756, ['fdfrere', 'fdsfwrw32']]
   list3 = copy.deepcopy(list1)
   list3[2][0]="tgtgte"
   print(list1)  # [234, 65756, ['fdfrere', 'fdsfwrw32']]
   print(list3)  # [234, 65756, ['tgtgte', 'fdsfwrw32']]
   ```

   

2. 深:将源对象的子对象内存地址重新分配给了一份给新对象,源对象和新对象的改变不会导致另外一个对象改变

3. 拷贝需要引入copy库,import copy



### 3.变量

#### 3.1 全局变量

1. python的全局变量和java的不一样,java中必须先定义类或接口,但是python中不需要.不在类和方法中定义的变量,全都是全局变量,从变量定义开始到文件结束的位置都可以使用,通常直接定义在文件开头

2. 函数内要访问或改变全局变量的值,必须先用global声明一下

3. 在类中可以直接调用全局变量,也可以修改

   ```python
   str1="fdsfds"
   class Test(object):
       print(str1)  # 可访问
       str1="gfdgfdgfd"  # 可改
   	def fn():
           print(str1)  # 抛异常,默认访问的是fn内部的str1,但是内部没有,故抛异常
   		global str1
   		print(str1)  # fdsfds,访问全局变量,因为已经声明了
   		str1="433543"
   		print(str1)	# 433543
   ```

4. 



#### 3.2 局部变量

1. 在函数体中声明的变量,形参
2. 若局部变量和全局变量同名,则在函数内部隐藏全局变量,只使用同名的局部变量



### 4.lambda表达式

1. lambda表达式类似js中的参数方法,定义之后必须赋值给一个变量

2. 只允许有一个表达式,不能包含复杂语句,表达式的结算结果就是函数的返回值

3. 表达式:

   > m=lambda arg1,arg2...argn: dosomething
   >
   > 调用:n=m(p1,p2...pn)



### 5.eval

> 将字符串当成有效的表达式进行求值并返回计算结果,和js中的eval一样,最好不要用
>
> 语法:eval(str[,dict[,arg]])->value
>
> str:需要执行的字符串
>
> dict:参数,该参数值中的键必须是str中的变量
>
> arg:可以是任意参数



### 6.递归(reduce)

> reduce(func,seq)必须有2个参数:
>
> 第一个参数是一个方法,用来计算第2个参数中的元素,且参数必须有2个,必须有返回值
>
> 第二个参数是方法作用的序列,可以是list,tuple,range等
>
> 运作原理:第一次调用方法时,会从seq中取得依次取得2个元素赋值给func中的2个参数,计算出结构得到返回值之后将会结果赋值给func的其中一个参数上,之后再从seq中取元素,再通过func计算,一直到seq中的元素取完



### 7.嵌套函数(内部函数)

> 在函数内部定义函数,且只能在函数内部调用该函数,外部不可调用,主要可以用来封装



### 8.global,nonlocal

#### 8.1 global

> 当在函数中要访问和修改全局变量时,需要先声明一下global,之后才可以访问和修改,见3.1全局变量

#### 8.2 nonlocal

> 在嵌套函数中需要访问外层的局部变量时,可以直接访问,但是不能修改.同样的也不能访问全局变量和修改全局变量.访问和修改全局变量需要声明global.若是需要修改外层的局部变量,需要在内部函数中声明nonlocal外层的局部变量,之后才可以修改

```
def fn1():
	a=1
	def fn2():
		print(a)  # 可访问
		a=5		# 不可修改,抛异常
		nonlocal a
		a=7		# 可修改
```



## 六.类

### 1.简介特性

1. 当解释器执行class语句时,就会创建一个类对象,不是实例对象
2. 可以多继承,子类的初始化方法中必须显示调用父类的init方法,否则系统默认不会初始化父类
3. 如果不继承任何类,默认继承object,和java一样
4. 子类会继承父类除了构造方法之外的所有属性和方法
5. 子类可以重写父类的同名方法,只要名字是一样的,就是重写
6. 若继承的多个父类中有重名属性和方法,若是没有特别指定,那么从左往右开始搜索继承父类中的第一个赋值

```python
class Test(parent1[,parent2]):
	def __init__(self,p1,p2):
        super().__init__(p1,p2)		# 显示调用父类构造函数,用super或直接用父类的类名
        parent1.__init__(self,p1,p2)
```



### 2.属性

#### 2.1 实例属性

> 1.初始化时赋值给self的属性,每个实例属性都不一样,不需要事先定义,在init的时候初始化
>
> 2.实例可以定义初始化没有的属性,每一个实例都是一个类似dict的对象,可以自由定义属性,类似js的object.但是实例定义的自由属性只能自己用,其他实例若使用该属性会抛异常

```python
class TestClass(object):
	# 构造方法,self必须是第一个参数,后面的都是参数,self相当于类本身,每次都会调用
    def __init__(self, *args1, **args2):
        # 赋值给类全局变量,该属性可以不定义,直接就赋值给self
        self.args1 = args1	# args1,args2都是实例化属性
        self.args2 = args2

t = TestClass()
t.name="哈哈"
print(t.name)	# 哈哈
t1 = TestClass()
print(t1.name)	# 抛异常
```



#### 2.2 类全局属性

> 定义在类中的属性,必须要赋值,也可以在类中的其他方法中随意调用,最好是通过类名调用

```python
class TestClass(object):
	str1 = "fdsfds"	# 类全局属性,必须先定义
	# 构造方法,self必须是第一个参数,后面的都是参数,self相当于类本身,每次都会调用
    def __init__(self, *args1, **args2):
        # 赋值给类全局变量,该属性可以不定义,直接就赋值给self
        self.args1 = args1	# args1,args2都是实例化属性
        self.args2 = args2
        TestClass.str1="fdswer"
```



#### 2.3 类私有属性

1. 以两个下划线开头的类变量被定义为私有属性,外部不能直接通过类名.类私有属性名访问
2. 类内部可以访问私有属性
3. 类内部可以通过类型.私有类属性名方法
4. 类外部仍然可以通过实例._类名私有属性名方法

```python
class TestClass(object):
	__str1 = "fdsfds"	# 类全局属性,必须先定义
	# 构造方法,self必须是第一个参数,后面的都是参数,self相当于类本身,每次都会调用
    def __init__(self, *args1, **args2):
        # 赋值给类全局变量,该属性可以不定义,直接就赋值给self
        self.args1 = args1	# args1,args2都是实例化属性
        self.args2 = args2
        TestClass.__str1="fdswer"	# 可访问
    def getStr1(self):
        return TestClass.__str1

# 类外部
t = TestClass()
print(t.getStr1())	# 返回fdsfds
print(t._TestClass__str1)	# 可访问,返回fdsfds
```



#### 2.4 特殊属性

```
obj.__dict__:对象的属性字典
obj.__class__:对象所属的类
class.__bases__:类的基类元素,多继承
class.__base__:类的基类
class.__mro__:类的继承层级结构
class.__subclasses__():类的子类列表
```





### 3.方法

> 类中方法可以分为固定方法(约定俗成)以及自定义方法.
>
> 固定方法已经由底层定义好,只需要适当重写即可.
>
> 自定义方法由人为定义
>
> 不管是固定方法还是自定义方法都可以通过self相互调用,不必管方法定义的先后顺序
>
> 方法不可以重载,若有方法名相同,只会解析后面的方法



#### 3.1 固定方法



##### 3.1.1 \_\_new\_\_(self)

> 在对象创建时调用,基本上不用重写,创建之后会调用init方法



##### 3.1.2 \_\_init\_\_(self)

1. 每次初始化都会调用,若是重写该方法,第一个参数必须是self,self代表当前对象,类似java中this
2. python没有方法重载,故而构造方法只能有1个,所以初始化时最好把其他需要初始化的操作一次完成.此时可以对实例化属性和类全局变量进行设置

```python
class TestClass(object):
	# 构造方法,self必须是第一个参数,后面的都是参数,self相当于类本身,每次都会调用
    def __init__(self, *args1, **args2):
        # 赋值给类全局变量,该属性可以不定义,直接就赋值给self
        self.args1 = args1
        self.args2 = args2
        print("我是每次默认都会调的,初始化方法,相当于构造")
        print(args1,args2)
        # 类中的方法可以相互调用,不必管定义的先后
        self.testGlobal()
```



##### 3.1.3 \_\_del\_\_(self)

1. 析构方法,对象被销毁时调用,del obj的时候会主动调用,或者垃圾回收器在对象没有引用时调用
2. 该方法的第一个参数必须是self,可不重写



##### 3.1.4 \_\_call\_\_(self)

1. 在类中没有该方法,若定义了该方法,表示该类的实例可以像函数一样被调用,注意是实例
2. 该方法的第一个参数同样必须是self



##### 3.1.5\_\_str\_\_(self)

1. 类似java中的toString()方法,默认的str方法输出的是类的类型



#### 3.2.自定义方法



##### 3.2.1 非静态方法

1. 第一个参数必须是self,实例和类都可以调用.
2. 类调用时第一个参数必须是实例对象,从第2个参数开始才是方法的参数,不必传self
3. 实例调用方法,不必传self,直接传参数即可



##### 3.2.2 类化

1. 在普通方法上添加注解@classmethod即可,必须紧挨着方法

2. 使用固定方法classmethod(方法名),只能传方法名,不能带括号也不能带参数,且需要赋值给变量

3. 必须传一个参数,该参数代表类,且必须是第一个.但是调用时该参数不用传,且不能访问类属性

4. 不管是类中的公有方法还是私有方法,类化后都可以直接用类名.方法名调用

   ```python
   class Test:
   	@classmethod
   	def test01(self[,arg]):
           print("test01");
       # 公有方法
       def test02(self[,arg]):
           print("test02");
       clsmethod1 = classmethod(test02)
       # 私有方法
       def __test01(self[,arg]):
           print("__test01");
       clsmethod2 = classmethod(__test01);
       
   Test.test01() # test01
   Test.clsmethod1()	# test02
   Test.clsmethod2()	# __test01
   ```



##### 3.2.3 静态方法

1. 和类本身没有关系,只能做纯粹的工具类.静态方法不能访问实例属性和实例方法,会抛异常

2. 方法上添加@staticmethod注解,可以使方法变为一个静态方法

3. def test1():不传self或类对象,编译器会报错,但是不用管.之后将该方法用固定方法staticmethod(test1)将会使该方法转换为一个静态方法

4. 不需要传任何特定的参数,可随意传参

5. 动态给类添加方法,注意是给类添加,而不是实例.需要函数可见,不在类中,而在module中

   ```python
   class Test:
       # 该方法会报错,但是不用管
       def test01([arg]):
           print("test01")
       static01 = staticmethod(test01)
       
   	@staticmethod
   	def test02([arg]):
   		print("test02")
   Test.static01()	# test01
   Test.test02()	# test02
   
   def test03():
       print("test03")
   Test.dynamicMethod = test03
   test1 = Test()
   test1.test03()	# test03
   ```



##### 3.2.4 私有方法

1. 私有方法的定义和访问同类私有方法



#### 3.3 特殊方法

##### 3.3.1 特殊类方法

```python
1.__new__(self):对象创建
2.__init__(self):构造方法,对象初始化
3.__del__(self):析构方法,对象回收
4.__repr__(self),__str__(self):打印,输出,print
5.__call__(self):函数调用,直接类名()调用
6.__getattr__(self):点运算,获得属性class.attra
7.__setattr__(self):点运算,属性赋值,class.attra=1
8.__getitem__(self):索引运算,a[key]
9.__setitem__(self):索引运算,赋值,a[key]=value
10.__len__(self):长度
```



##### 3.3.2 特殊运算符方法

```
__add__():+,加法
__sub__():-,减法
__lt__(),__le__(),__eq__():<,<=,==
__gt__(),__ge__(),__ne__():>,>=,!=
__or__(),__and__(),__xor__():|,&,^,或,与,异或
__lshift__(),__rshift__():<<,>>,左移,右移
__mul__(),__truediv__(),__mod__(),__floordiv__():*,/,%,//,乘法,浮点触发,取余,整除
__pow__():**,幂,指数运算
```



### 4.注解

#### 4.1 @property

> 该注解只能用于类中方法上,标注了该注解的方法可以让类的实例直接像调用属性一样调用
>
> 若是像调用方法一样调用,那么方法的返回值将会被再调用一次,根据实际情况,是否报错或执行
>
> 只能访问添加了该注解的方法,但是不能进行修改

```python
class Test:
	@property
	def test01(self):
		print("test01")
	@property
	def test02(self):
		return "test02"
	@property
	def test03(self):
		return test02
	
t = Test()
print(t.test01)	# 先打印test01,test01方法没有返回值,输出None
t.test01()	# 抛异常,因为t.test01会先调用,返回一个None,进而再调用None(),该方法无法被调用,抛异常
def test04():
	print("test02")
print(t.test02)	# 输出test02
print(type(t.test02))	# <class 'str'>
t.test02()		# 抛异常,因为返回的是一个字符串,字符串无法被调用
t.test03		# 输出一个类型一个类型,因为test03方法返回的是一个方法指针
t.test03()		# 打印test02,真正的方法调用
```



#### 4.2 @classmethod

> 添加该注解的方法将直接被类化,之后可以被对象直接调用,而不需要实例化



#### 4.3 @staticmethod

> 静态化方法,标注了该注解的方法实际上和类并不任何关系,纯粹的工具类



### 5.使用类

1. 在类定义的module中使用,可以不用引入该类,直接使用
2. 类实例化时,self参数不需要传,如s=TestClass(),若构造函数init中有不可变参数,初始化时必须传参,否则抛异常

```python
class TestClass(object):
	# 构造方法,self必须是第一个参数,后面的都是参数,self相当于类本身,每次都会调用
    def __init__(self,name, *args1, **args2):
        # 赋值给类全局变量,该属性可以不定义,直接就赋值给self
        self.args1 = args1
        self.args2 = args2
        print("我是每次默认都会调的,初始化方法,相当于构造")
        print(args1,args2)
        # 类中的方法可以相互调用,不必管定义的先后
        self.testGlobal()
    def __test01(self):
        print("test01");
   
t = TestClass("name")
t1 = TestClass()	# 抛异常,必须传name参数
```





## 七.文件操作

### 1.文件打开模式

1. file=open(filepath[,mode[,encoding]]):打开文件,常用的3个参数,其他参数可查文档

   > filepath:文件路径,可以相对路径,也可以是绝对路径
   >
   > mode:文件的打开模式
   >
   > encoding:字符编码

2. r:只读,r+读写,追加

3. w:覆盖写,文件存在则直接覆盖源文件,没有就创建一个新文件,w+读写(有问题,不要用)

4. a:追加写入,不能读,a+读写

5. b:打开二进制文件,U支持�?有换行符

6. with也可以打开文件,并且不用关心忘记关掉文件,会自动关闭文件

7. 文件的seek和tell方法,都是以字节为单位来操作指针,但是read和write方法都是以字符来读写数据



### 2.文件读取

1. file.read():一次性将文件内容全部读取,若只是读取文件或只是写文件,没有其他操作,可进行链式调用
2. file.readline():读一行,根据换行符来判断
3. file.readlines():将文件中所有内容的每一行内容加上换行符读取到一个list中
4. 打开之后的文件可以直接用for循环进行读取,而且内存中读到那一行,就只存那一行,对比较大的文件比较友好

```
read1 = open("testFile.txt", 'r',encoding="utf8");  # 可链式调用open("file").read()
# print(read1.read());    # 读所有
print(read1.readlines())    # 读所有,将每行内容加上换行符读取到一个list中
print(read1.readline());   # 读一行,空,因为指针已经到结尾了,再读就没有了
read1.close();
read2 = open("testFile.txt", 'r',encoding="utf8"); 
for l in read2:	# 按顺序一行一行的读,在内存中也只存一行,对内存消耗比较小
    print(l)
read2.close()
```



## 八.常用类,方法

#### 1.time

> 需要引入time类,import time

1. time.time():返回1970.1.1到当前时间的秒数,小数点后的微秒,前3位是毫秒,加上后3位表示微秒

#### 2.random

> 需引入random,import random

1. random.shuffle(list):将列表中元素的顺序随机打乱