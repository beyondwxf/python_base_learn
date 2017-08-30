'''
Created on 2017年8月30日

@author: hexun
内置装饰器
'''

#类方法 ：与成员方法的区别在于所接收的第一个参数不是self（类实例的指针），而是cls（当前类的具体类型）

#属性方法 ： 将一个类方法变成一个类属性，只读属性
#property

 
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
    
    @property
    def say_property(self):
         print(self.__money)
         return self.name
     
    @classmethod
    def say(self):
         print(self.__money)
         
    @staticmethod
    def bye():
         print('静态方法不用创建对象 直接调用')
         
Human.bye()
Human.say()

tom = Human('tom',20)
print(tom.say_property)



class Person:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def full_name(self):        
        return "%s%s" % (self.first_name,self.last_name)

f1 = Person('mile','diergess')
flname = f1.full_name()
print(flname)

