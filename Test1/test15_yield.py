'''
Created on 2017年8月29日

@author: hexun
生成器 yield 惰性返回
'''


def f1():
    return 1



def f2():
    yield 1
    yield 2
    yield 3

g = f2()
print(g.__next__())
print(g.__next__())
print(g.__next__())
