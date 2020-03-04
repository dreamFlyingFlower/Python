'''
加密算,包含了md5
'''
import hashlib
import hmac
m=hashlib.md5()
m.update(b"Hello")  # 若使用二进制则不支持中文
m.update("我是谁".encode(encoding="utf8")) # 中文需要先编码
m.update(b"World")  # update是每次都拼接上上一次update的值进行加密,中间无空格
print(m.digest())
print(m.hexdigest())    # 返回二进制进行16进制编码之后的字符串,68e109f0f40ca72a15e05cc22786f8e6
m2=hashlib.md5()
m2.update(b"HelloWorld")
print(m2.hexdigest())   # 和前面2次update的值一样,68e109f0f40ca72a15e05cc22786f8e6
hh = hmac.new(b"key", b"我msg", "md5")   # 不支持中文,若使用中文需要先encode
hh.update(b"value")
print(hh.hexdigest())