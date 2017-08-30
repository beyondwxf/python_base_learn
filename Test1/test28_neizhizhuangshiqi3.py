'''
Created on 2017年8月30日

@author: hexun
内置装饰器
'''
#类静态方法:与成员方法的区别是没有self参数，并且可以在类不进行实例化的情况下调用
#staticmethod
from decimal import Decimal

#类方法 ：与成员方法的区别在于所接收的第一个参数不是self（类实例的指针），而是cls（当前类的具体类型）
#classmethod

#属性方法 ： 将一个类方法变成一个类属性，只读属性
#property


class Fees (object):
    def __init__(self):
        self.__fee = None
    
    def get_fee(self):
        return self.__fee
    
    def set_fee(self,value):
        if isinstance(value, str):
            self.__fee = Decimal(value)
        elif isinstance(value, Decimal):
            self.__fee = value

fee = Fees()
print(fee.get_fee())
fee.set_fee('10.0')
print(fee.get_fee())