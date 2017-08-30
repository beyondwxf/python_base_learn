'''
Created on 2017年8月30日

@author: hexun
内置装饰器
'''

class Human:

    name = 'ren'
    gender = 'male'
    age = '25'
    #私有属性new 直接是无法取
    __money = 808080
    
    #初始化方法
    def __init__(self,name,age):
        print('#'*50)
        self.name = name 
        self.age = age
        
    def __str__(self):
        msg = 'ssssssssss'
        return msg
    
    def say(self):
         print(self.__money)
         self.__lie()
         
