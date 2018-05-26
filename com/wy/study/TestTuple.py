'''
Created on 2018年5月26日

@author: wanyang
    tuple:元组,相当于数组,但是可存任何类型的数据,并且当只有一个元素的时候,必须加上逗号
        否则会被认为是某一个单一类型的数据
    定义元组:ex=(3,'6565');ex1=(3,);
    元素的操作可以和字符串的切片操作差不多
'''
# 可将元组的元素赋值给等同数量的变量,若不等同,会报错
import com.wy.study.TestStr as testStr

str1,str2,str3 = ("434","rer","rerte");
print(str1,str2,str3)
print(__name__)
print(testStr.__name__)