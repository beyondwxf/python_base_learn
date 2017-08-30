'''
Created on 2017年8月30日

@author: hexun

异常
'''
try:   
    s = 'hello'
    print(s[10])
except IndexError:
    print('error')
else:
    print('no error')
    
    
try:
    f = open('filetestr.txt','r')
    fr = f.read()
    print(fr)
finally:
    f.close()
    
#文件用with as  会自动关闭
with  open('filetestr.txt','r') as f:
    print(f.read())
    
    
#raise 异常名字:
#raise 异常名字 附加信息
#assert 语句（True/False）
if 1:
    raise NameError('your name error!!!')

l = [1]
assert len(2),'changdu'