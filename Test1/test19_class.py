'''
Created on 2017年8月30日

@author: hexun
公有属性
名字
私有属性
__名字
'''
class Car:
    color = ''
    
    def run(self):
        print('go go go！')

bmw = Car()
bmw.color = 'red'
print(bmw.color)
print(bmw.run())