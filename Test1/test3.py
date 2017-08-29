'''
Created on 2017年8月24日

@author: hexun

'''
hp = 100
print('welcome heros world')
name = input('input your name:')
if not name:
    name = 'play1'

userMsg = [name,hp]
print('your hero name is :',userMsg[0])