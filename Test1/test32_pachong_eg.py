'''
Created on 2017年9月1日

@author: hexun
 小爬虫获取当前页面的图片
'''
import re
import urllib.request



def  getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    html=html.decode('utf-8')#python3
    reg = r'bpic="(.*?\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(reg, html)
    print('imglist:',imglist)
    x = 0
    for imgurl in imglist:
        print(imgurl)
        urllib.request.urlretrieve(imgurl, '%s.jpg' %x)
        x+=1
url = 'http://tieba.baidu.com/f?kw=%E5%BC%80%E5%AD%A6&red_tag=f2036529020'
print(getHtml(url))

print('kaishi')
getImg(getHtml(url))
print('jieshu')