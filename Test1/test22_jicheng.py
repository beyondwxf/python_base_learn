'''
Created on 2017年8月30日

@author: hexun
继承只能用公有属性的共有方法，不能继承私有属性的私有方法

多继承 如果变量和方法重名，只能继承第一个
'''
class Father:
    money = 10000
    __money = 10000
    
    def driver(self):
        print('i can driver a car!')
        
class Mother:
    money = 10000


class Son(Father,Mother):
    def pay(self):
        print(self.money)

tom = Father()
print(tom.money)
tom.driver()

print('#'*50)

jerry = Son()
print(jerry.money)
jerry.driver()
jerry.pay()