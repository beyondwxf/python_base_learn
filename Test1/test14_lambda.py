'''
Created on 2017年8月29日

@author: hexun
'''
from _functools import reduce
def myadd (x,y):
    return x+y

a = [1,2,3,4,5,6,7,8,9]

#累加
print(reduce(myadd, a))

#lambda表达式前两个是参数 后面是运算
print(reduce(lambda x,y:x*y, a))


#filter()

#zip()

#map()

foo = [2,18,9,22,17,24,8,12,27]

foo_filter = filter(lambda x:x%3 == 0,foo)
print('==============foo_filter=============')
for i in foo_filter:
    print(i)
print('==============foo_filter=============')


foo_map = map(lambda x:x*2 + 10,foo)

print('==============foo_map=============')
for i in foo_map:
    print(i)
print('==============foo_map=============')