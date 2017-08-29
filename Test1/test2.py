#!/usr/bin/env python
  
import getpass
  
name = "Bourbon"
passwd = "abc123"
  
username = input('请输入用户名:')
password = getpass.getpass('请输入密码:')
 
if username == name and password == passwd:
    print('ssss')
else:
    print ('用户名或密码错误！')