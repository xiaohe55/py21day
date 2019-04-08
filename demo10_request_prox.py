# -*- coding:utf-8 -*-
'''
@author:coyote
@datetime:2019/4/8 23:30
@file: demo10_request_prox.py
@function:搜免费代理
'''
import requests

proxy = {
    'http': '111.206.6.100:80'
}
response = requests.get('http://httpbin.org/ip', proxies=proxy)
print(response.text)
