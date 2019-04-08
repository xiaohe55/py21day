# -*- coding:utf-8 -*-
'''
@author:coyote
@datetime:2019/4/8 7:20
@file: demo7.py
@function:保存cookie信息到本地
'''
from urllib import request
from http.cookiejar import MozillaCookieJar

cookiejar = MozillaCookieJar('cookie.txt')
# 加载cookie
cookiejar.load(ignore_discard=True)
handler = request.HTTPCookieProcessor(cookiejar)
opener = request.build_opener(handler)

resp = opener.open('http://httpbin.org/cookies')

for cookie in cookiejar:
    print(cookie)

# 保存cookie信息
# cookiejar.save(ignore_discard=True)
