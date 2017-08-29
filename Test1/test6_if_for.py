'''
Created on 2017年8月25日

@author: hexun
'''
'''
if 条件:
        代码块
elseif 条件 :
     代码块
else:
     代码块   
     
for 迭代量  in 序列:
    代码块
    
while 条件:
    代码块
'''

for i in 'hello':
    print('aaaa')

for i in 'hello':
    print(i)
    
for x in range(10):
    print(x)
    
for x in range(1,10):
    print(x)

for x in range(1,10,2):
    print(x)
    
for i in range(10):
    if i == 5:
        print(i)
        continue
    if i == 7:
        break
    #pass占位符
    if i == 7:
        pass
    print(i)
