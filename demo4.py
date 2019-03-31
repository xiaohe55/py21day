# -*- coding:utf-8 -*-
'''
@author:coyote
@datetime:2019/3/28 22:55
@file: demo4.py
@function:快代理，西刺代理
ProxyHandler 处理器，（代理）
1. 代理原理：在请求目的网站之前，先请求代理服务器。
    然后让代理服务器去请求目的网站，代理服务器拿到目的网站的数据后，再转发给我们的代码
2. https://httpbin.org/ 查询HTTP请求的参数
3. 在代码中使用代理
    1' 使用 url.request.ProxyHandler传入一个代理，这个代理是一个字典，
    字段的key依赖于代理服务器能够接受的类型，一般为HTTP或HTTPS，值为"ip:port"
    2' 使用上一步创建的“handler”，以及“request.build_opener”创建一个“opener”对象
    3' 使用上一步骤的"opener"，调用open函数，发起请求
'''

from urllib import request

# 没有使用代理
# url = 'https://httpbin.org/ip'
# resp = request.urlopen(url)
# print(resp.read())

# 使用代理的
url = 'http://httpbin.org/ip'
# 1.使用ProxyHandler，传入代理构建一个hander
handler = request.ProxyHandler({'https': '119.57.108.109:53281'})
# 2.使用上面创建的handler构建一个opener
opener = request.build_opener(handler)
# 3.使用opener发送一个请求
resp = opener.open(url)
print(resp.read())
