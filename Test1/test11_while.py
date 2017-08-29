'''
Created on 2017年8月28日

@author: hexun
'''
import os
welcome = 'welcome to Heroes world!'

i = 0
while True:
    #验证文件是否存在
    if os.path.isfile('lock.log'):
        print('locked')
        break
    username = input('login:')
    password = input('password:')
    
    i += 1 
    if username == 'milo' and password == '123':
        print(welcome)
    else:
        if i == 3:
            #没有就创建
            open('lock.log', 'w').write(username)
            print('locked by %s'%username)
            break