'''
Created on 2017年8月25日

@author: hexun
字典
{'key':'value','key':'value'}
'''
dict2 = {'s':'1','a':'2'}
print(dict2['s'])


dict2['p'] ='3'

print(dict2)


print(dict2.get('s'))

print(dict2.get('12313','这个值默认为空，如果不设置则返回空，设置如果key对用值没有则返回后面这个值'))

x = 10
y = 11
dict = {'s':x,'a':y}

#字典实现swich
