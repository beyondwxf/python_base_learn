'''
Created on 2017年8月28日

@author: hexun
fileobject = open(filename,tpye)

第一个参数文件路径名字
第二个打开方式读r 还是写 w(重建文件)
a 写入 在文件末尾追加新内容 如果没有创建
+ 更新
b 打开二进制的文件
U 支持所有的换行符号 
'''

s1 = open('filetestr.txt','r')
s2 = open('filetestr.txt','r+')
s3 = open('abc','a+')
b = open('filetestw.txt','w+')
print(s1.readline())
print(s1.readlines(3))
print(s1.readlines())
print(s1.read())


b.write('123123')
s1.close()
s2.close()
s3.write('axs')
'''
设置指针偏移量
seek(偏移量，选项)
选项=0时，标识将文件指针指向从文件头部到偏移量字节处
选项=1时，标识将文件指针指向从文件的当前位置，向后移动偏移量字节
选型=2时，表示将文件指针指向从文件的尾部，向前移动偏移量字节
'''



s3.seek(1,0)
#提交
s3.flush()
s3.close()
b.close()