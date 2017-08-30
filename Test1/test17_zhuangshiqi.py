'''
Created on 2017年8月30日

@author: hexun
 装饰器
'''

import time

def deco(func):
    #设置伪函数返回，嵌入传入函数
    def wrapper():
        startT = time.time()
        func()
        endT = time.time()
        msecs = (endT - startT)*1000
        print("it's %f ms" % msecs)
    return wrapper

@deco
def myfunc():
    print('myfunv start...')
    time.sleep(1.7)
    print('myfunc end...')


#函数调用属性
print("myfuns is ",myfunc.__name__)

#把函数传进去  等同于在@deso  
#myfunc = deco(myfunc)

print('#'*50)
#函数调用属性
print("myfuns is ",myfunc.__name__)
myfunc()


