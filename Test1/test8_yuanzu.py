'''
Created on 2017年8月25日

@author: hexun
元组
不可变的元组和灵活的列表
'''

t = ('x','y','z')
a,b,c = t 
print(a)
print(b)
print(c)

print('$$$$$$$$$$$$$$$')

nums = []
for i in range(1,1000):
    if i%3 == 0 or i%5 == 0:
        nums.append(i)
print(sum(nums))

print('#'*50)
#列表解析 一个列表 到 另一个列表
print([i*10 for i in range(10)])

print([i*10 for i in range(10) if i > 5])

print([i for i in range(10) if i%3==0 or i%5==0])

print(sum([i for i in range(10) if i%3==0 or i%5==0]))

#生成器表达式惰性查询触发，效率高些
print((i for i in range(10) if i%3==0 or i%5==0))


e = ['a','b','c']
d = ['1','2','3']
#zip 变成这样的数据[('a','1'),('b','2'),('c','3'),]
e = zip(a,d)

print((i for i in e ))

for i in e:
    print(i)
    

def f(x,y):
    print("%s %s" %(x,y))
    
    
a = ('s','1')
#元组传值
f(*a)

#传字典就要两个**号

def f1(name,age):
    print("%s %s" %(name,age))

a1 = {'name':'zhangsan','age':'10'}

f1(**a1)

#多个传参
def f3(x,*args,**kwargs):
    print( x )
    print( args )
    print( kwargs )
    
f3(1)
f3(1,2,3,4,5,6)