'''
Created on 2017年8月30日

@author: hexun
内置装饰器
'''
#类静态方法:与成员方法的区别是没有self参数，并且可以在类不进行实例化的情况下调用
#staticmethod

#类方法 ：与成员方法的区别在于所接收的第一个参数不是self（类实例的指针），而是cls（当前类的具体类型）
#classmethod

#属性方法 ： 将一个类方法变成一个类属性，只读属性
#property



class Person:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        
    @property
    def full_name(self):        
        return "%s %s" % (self.first_name,self.last_name)

f1 = Person('mile','diergess')
print(f1.full_name)

