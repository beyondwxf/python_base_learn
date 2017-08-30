'''
Created on 2017年8月30日

@author: hexun
闭包
闭包函数必须有内嵌函数
内嵌函数需要引用该嵌套函数上一级变量
闭包函数必须返回内嵌函数
'''
def hello_conf(prefix):
    def hello(name):
        print(prefix,name)
    return hello

a = hello_conf('good morning')
a('milo')
a('zouqixian')
print(a.__name__)
print(id(a))

b = hello_conf('good afternon')
b('milo')
b('zouqixian')
print(b.__name__)
print(id(b))