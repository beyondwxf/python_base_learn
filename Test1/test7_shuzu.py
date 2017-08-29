'''
Created on 2017年8月25日

@author: hexun
'''
a = [1,3,34,56,21]
b = [4,5,1,2,3,8]
c = ['c','d']
d = [1,3,34,56,21]
a = a + b
#负数为倒序 数据为隔几个取一个
print(a[::-1])
print(a[::-2])
print(a[::2])
for i in a:
    print(i)

print('#######')
#b.append(100)
#b.insert(3, 135)
b.append(c) #数组会直接被追加
b.extend(c) #数组会被拆出来再追加
print('pop:', b.pop(1))
print('count:', b.count(10))
print('remove:', b.remove(1))

for i in b:
    print(i)

print('@@@@@@')

d.sort(reverse=True)

for i in d:
    print(i)

print('=================')

