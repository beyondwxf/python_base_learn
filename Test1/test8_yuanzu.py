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

#列表解析 一个列表 到 另一个列表
print([i*10 for i in range(10)])

print([i*10 for i in range(10) if i > 5])

print([i for i in range(10) if i%3==0 or i%5==0])

print(sum([i for i in range(10) if i%3==0 or i%5==0]))

#生成器表达式惰性查询触发，效率高些
print((i for i in range(10) if i%3==0 or i%5==0))
