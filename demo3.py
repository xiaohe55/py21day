# -*- coding:utf-8 -*-
'''
@author:coyote
@datetime:2019/2/15 8:28
@file: demo3.py
@function:
'''

from urllib import request, parse

url = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='

# 错误代码
# resp = request.urlopen(url)
# print(resp.read())

# 已经被禁
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
# req = request.Request(url, headers=headers)
# resp = request.urlopen(req)
# print(resp.read())


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Referer': 'https://www.lagou.com/jobs/list_python?city=%E5%8C%97%E4%BA%AC&cl=false&fromSearch=true&labelWords=&suginput='}
data = {
    'first': 'true',
    'pn': 1,
    'kd': 'python'
}
req = request.Request(url, headers=headers, data=parse.urlencode(data).encode("utf-8"), method="POST")
resp = request.urlopen(req)
print(resp.read().decode('utf-8'))
