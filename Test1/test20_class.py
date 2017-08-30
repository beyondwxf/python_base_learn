'''
Created on 2017年8月30日

@author: hexun
公有属性
名字
私有属性
__名字

私有方法 一样 

def __method

特殊的方法
__init__() 构造函数，声称对象时自动调用

魔法方法  类似tostring 打印对象的时候 返回
__str__
'''
class Human:
    '''
        我是doc说明我是doc说明我是doc说明我是doc说明我是doc说明
        
    '''
    
    
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
         
    def __lie(self):
        print('woshi lie')
    
zs = Human('lisi',10)
zs.name = 'zhangsan'
print(zs.name)
#私有属性new 直接是无法取
#print(zs.__money)
#print(zs.__lie)
zs.say()

lisi = Human('lisi',10)
#lisi.say()

print(lisi.__str__())

print(Human.__doc__)