'''
Created on 2017年8月28日

@author: hexun
函数

len()
divmode()
'''
import random
from builtins import divmod, isinstance, str
from _ast import Str
import string

def apple (hp) :
    hp += 10
    return hp 

def boom (hp) :
    hp += 10
    return hp 

a = random.randint(1,100)
print(a)

s1 = 'ssssss'
s2 = ['1','2','3']
s3 = -1
print(s1.__len__())
print(len(s2),len(s1))

#本函数是实现a除以b，然后返回商与余数的元组。如果两个参数a,b都是整数，那么会采用整数除法，
#结果相当于（a//b, a % b)。如果a或b是浮点数，相当于（math.floor(a/b), a%b)。
print(divmod(10,3))
#函数是计算x的y次方，如果z在存在，则再对结果进行取模，其结果等效于pow(x,y) %z
print(pow(10, 4))
#绝对值
print(abs(-11))

print(max(s2))
print(min(s2))
#语法：isinstance（object，type）

#作用：来判断一个对象是否是一个已知的类型。 
#语法：isinstance（object，type）
#作用：来判断一个对象是否是一个已知的类型。 
#其第一个参数（object）为对象，第二个参数（type）为类型名(int...)或类型名的一个列表((int,list,float)是一个列表)。其返回值为布尔型（True or flase）。
#若对象的类型与参数二的类型相同则返回True。若参数二为一个元组，则若对象类型与元组中类型名之一相同即返回True。
a = "b"
print(isinstance(a,int))
print(isinstance(a,(int,list,float,str)))
#1. 方法用来检测对象是否可被调用，可被调用指的是对象能否使用()括号的方法调用。
#2. 可调用对象，在实际调用也可能调用失败；但是不可调用对象，调用肯定不成功。
#3. 类对象都是可被调用对象，类的实例对象是否可调用对象，取决于类是否定义了__call__方法。
callable(apple(2))

for i in range(1,10):
    print(i)
    
#str()字符串
#list()数组
#tuple()元组

#16进制
print(hex(1))
#8进制
print(oct(10))
print('=============')
#ASCII
#print(chr('a'))
#将ASCLL码值转换为字符 
print(ord(128))

#首字母大写
str.capitalize()
#替换
#str.replace(old, new)
#分割 第一个参数以什么分割，第二个参数最大分割次数
#str.split(sep=None, maxsplit=_1)


#声明：s为字符串，rm为要删除的字符序列

#s.strip(rm)        删除s字符串中开头、结尾处，位于 rm删除序列的字符

#s.lstrip(rm)       删除s字符串中开头处，位于 rm删除序列的字符

#s.rstrip(rm)      删除s字符串中结尾处，位于 rm删除序列的字符

str.strip()


#str.join(iterable)
help(string)

#字典
#字典的可以值
dict.keys()
#字典值
dict.values()
#字典所有项
dict.items()
#字典返回值
dict.get('y')
