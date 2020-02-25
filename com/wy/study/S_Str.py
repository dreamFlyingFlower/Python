str1 = "qwertyuiop"
# slice,切片.截取下标为1到4的字符串,含头不含尾,返回一个新的字符串
print(str1[1:4])
# 截取字符串,根据最后一个参数,从第一个开始(截取后的字符串加上第一个),
# 依次加上最后一个参数的下表长度截取字符串,知道超出该字符串长度
# 冒号的第三个参数是间隔多少个字符串截取
print(str1[::2])
print(str1[1:6:2])  # 从1到6,隔下标2截取字符串
print(str1[-3:])  # 倒数截取字符串
print(str1[1:900])
# print("fdfd"+123)       # 报错
s = str1.split()
print(type(s))
print(len(s))
print(s)
# print(str1.split(""))       # 报错
str3 = "fdd fdfd wrew dfgfd"
print(str3.split())
print(str3.split(" "))  # 不报错,等同于str1.split()
print(str.split(str3))  # 等同于str3.split()
list1 = ["34", "re", "34", "fgdg"]
print("||||".join(list1))
str.join
print(str.join("||||", list1))  # 等同于"||||".join(list1)
str4 = "fds_r3wefwfter43543h_htytr#%^"  # 不管字符串中的内容是如何,使用is和==得到的都是true,不管带不带特殊字符
str5 = "fds_r3wefwfter43543h_htytr#%^"
print(str4 is str5)
print(id(str4))
print(id(str5))
print("fd" in str5)
# print(3 in str5)        # 抛异常
print(not "df" in str5)
print("df" not in str5)  # 等同于not "df" in str5
print(str5.startswith("ffff"))
print(str.startswith(str5, "ffff"))
print(str5.find("_", 8))
print(str.find(str5, "_", 8))
print(str.count(str5, "_"))
print(str5.count("_"))
print(str.isalnum(str5))
print(str5.isalnum())
print("545gfd4佛挡杀佛".isalnum())  # true,全是数字和字母汉字,不带特殊字符,如_
print("545gfd4佛挡杀佛_".isalnum())  # false
print("---------------------")
print("dfdf我东方舵手".isalpha())  # true,全是字符和汉字,不能带数字
print("dfdf245我东方舵手".isalpha())  # false
print(str.isdigit("432432"))  # true,是否全是数字
print("   fdfd: ".strip())
print(str.strip("    fdfd:  "))
print(" fdfd   ".lstrip())
print(str.lstrip("   fddf"))
print(str.rstrip("   fdfd", "d").lstrip())
print(str.capitalize(str5))
print(str.title(str5))
print(str.swapcase(str5))
print(str.center("fdfd", 11, "|"))
print("".isspace())
print("324.5".isnumeric())
print(str.format("test{0}fdsew温热我{1},{0}","而烦到死","放松放松的","发达省份温热"))
# print(str.format("范德{name},{tttt},{name},那么{beauty}",name="dfsfds",tttt="外人23"))# 错误,抛异常,参数必须对应,不能少
print(str.format("我是{0},hi好{1:|^10}","秒","giao"))
print(str.format("我{name},{tt:|^10}",name="方法",tt="MM"))
import io
str9 = "qwertyuiop"
str9 = io.StringIO(str9)
print(str9.getvalue())
str9.seek(30)
print(str9.getvalue())
print(len(str9.getvalue()))
str9.write("23fdsfdsfdsfewrew43543534")
print(str9.getvalue())
