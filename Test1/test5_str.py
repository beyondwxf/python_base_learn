'''
Created on 2017年8月24日

@author: hexun
'''
a = "jsjlsj %s ssdlsjdj %ad !"
b = 'abcdefghi abcdefghi'
c = '192.7.51.1'
print(a%(888,999))
print(b[0:4])
print(b[0:2:4])
#返回首字母大写
print(b.capitalize())
print(b.count('a'))
print(b.find('de'))
print(b[6:11])
print(b[b.find('de'):11])
ip = c.split('.')
print(ip)
e ='--'.join(ip)
print(e)
