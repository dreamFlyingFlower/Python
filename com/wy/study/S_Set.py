# set1=set(1,2,3,4,5,5,5) # 错误
set1={12,545,767,83,34,34}
print(set1)
# set1.remove(56) # 抛异常
set1.remove(12)
print(set1)
# del set1(545)
print(set1)
set2=set1.union({23,65,"6546"})
print(set1)
print(set2)
set3=set([34,83])
print(set3.issubset(set1))
set1.add(77)
print(set1)
print(set2.discard(34))
print(set2)