'''
Created on 2017年8月29日

@author: hexun

导入
import  模块    as 别名

form  模块名  import  函数/类名 /*
'''


name = 'this is sjdlkajdjalj '

def show():
    print('hello this is mymoulell')
    
print(__name__)
#直接运行模块__name__属性的值是否为__main__判断  直接运行模块才执行，间接调用则不执行
if __name__ == '__main__':
    print(show())