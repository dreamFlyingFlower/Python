a = {}
a.setdefault("key", "222")
a.setdefault("key1", "44")
a.setdefault("key2", 55)
a.setdefault("key3", 57)
a.setdefault("key4", 59)
# 同时遍历key,value
for k,v in a.items():
    print(k)
    print(v)
for item in a.items():
    print(item)  # 元组
print("-------------")
print(a)
print(a.get("key5"))
print(a.get("key5", 333))
a.__delitem__("key")
# del(a["key2"])
# del a["key1"]
# b = a.pop("key3")
c=a.popitem()
print(c)
print(type(c))
# a.clear();
print(a)

