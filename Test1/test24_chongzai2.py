'''
Created on 2017年8月30日

@author: hexun
继承只能用公有属性的共有方法，不能继承私有属性的私有方法

多继承 如果变量和方法重名，只能继承第一个
'''

class Mylist:
    __mylist = []
    
    def __init__(self,*args):
        self.__mylist = []
        for i in args:
            self.__mylist.append(i)
            
    def __add__(self,x):
        for i in range(0,len(self.__mylist)):
            self.__mylist[i] = self.__mylist[i]+x
        print(self.__mylist)
        
    def __sub__(self,x):
        pass
    
            
        
l = Mylist(1,2,3,4,5)
l+10