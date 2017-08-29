'''
Created on 2017年8月28日

@author: hexun
可变集合 set
无序排序且不重复，是可变的

不可变集合 frozenset
冻结的集合，不可变
'''
x = set('hello')
y = set('world')
x.add('12')
x.add('333')
print(x)
print(y)
#交集
c = x & y
print(c)
#合集
d = x | y
print(d)
#补集
e = x - y 
print(e)

x.remove('333')

print(x)