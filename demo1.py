# -*- coding:utf-8 -*-
'''
@author:coyote
@datetime:2019/2/14 8:09
@file: demo1.py
@function:urlopen
'''
from urllib import request
from urllib import parse

'''
urlopen
'''
# resp = request.urlopen('http://www.baidu.com')
# 读取全部
# print(resp.read())
# 读取10个字符
# print(resp.read(10))
# 读取第一行
# print(resp.readline())
# 读取多行
# print(resp.readlines())
# 状态码
# print(resp.getcode())


'''
urlretrieve:下载网页到本地
'''
# 下载百度网页
# request.urlretrieve("http://www.baidu.com", 'baidu.html')
# 下载图片
# request.urlretrieve("https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=3780996643,1336778904&fm=26&gp=0.jpg", 'modi.jpg')

"""
urlencode 编码
"""
# params = {"name": "张三", "age": 18, "greet": "hello world"}
# result = parse.urlencode(params)
# print(result)

# url = "http://www.baidu.com/s"
# params = {"wd": "刘德华"}
# qs = parse.urlencode(params)
# url = url + "?" + qs
# resp = request.urlopen(url)
# print(resp.read())

"""
parse_qs 解码
"""

# params = {"name": "张三", "age": 18, "greet": "hello world"}
# qs = parse.urlencode(params)
# print(qs)
# result = parse.parse_qs(qs)
# print(result)


