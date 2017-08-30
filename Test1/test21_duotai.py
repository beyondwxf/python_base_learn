'''
Created on 2017年8月30日

@author: hexun
'''
class Triangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        
    def getArea(self):
        area = self.width * self.height/2
        return area

class Square:
    def __init__(self,size):
        self.size = size
        
    def getArea(self):
        area = self.size * self.size
        return area

a = Triangle(5,5)
print(a.getArea())
b = Square(5)
print(b.getArea())
        