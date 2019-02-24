# -*- coding:utf-8 -*-
'''
@author:coyote
@datetime:2019/2/15 8:17
@file: demo2.py
@function: urlparse & urlsplit
两个函数几乎一模一样，唯一区别urlsplit缺少params属性
'''

from urllib import parse

url = "http://www.baidu.com/s?wd=python&username=abc#1"
"urlparse"
result = parse.urlparse(url)
print(result)
print("scheme:", result.scheme)
print("netloc:", result.netloc)
print("path:", result.path)
print("params:", result.params)
print("query:", result.query)
print("fragment:", result.fragment)

"urlsplit"
result = parse.urlsplit(url)
print(result)
print("scheme:", result.scheme)
print("netloc:", result.netloc)
print("path:", result.path)
# print("params:", result.params)# 没有这个参数
print("query:", result.query)
print("fragment:", result.fragment)
