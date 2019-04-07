# -*- coding:utf-8 -*-
'''
@author:coyote
@datetime:2019/3/31 23:28
@file: demo6.py
@function:没有成功
人人登录：http://sns.renren.com/
百度个人主页： http://www.renren.com/880151247/profile
'''
from urllib import request
from urllib import parse
from http.cookiejar import CookieJar

# 1.登录
# 1.1 创建一个cookiejar对象
cookiejar = CookieJar()
# 1.2 使用cookiejar创建一个HTTPCookieProcess对象
handler = request.HTTPCookieProcessor(cookiejar)
# 1.3使用上一步创建的handler创建一个opener
opener = request.build_opener(handler)
# 1.4使用opener发送登录的请求（人人网邮箱密码）
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}
data = {
    "email": 'zhuzhanji1',
    'password': '881106'
}
login_url = 'http://sns.renren.com/'
req = request.Request(login_url, data=parse.urlencode(data).encode('utf-8'), headers=headers)
opener.open(req)
# 2.访问个人主页
dapeng_url = 'http://www.renren.com/880151247/profile'
# 获取个人主页的页面的时候，不要新建一个opener
# 而应该使用之前的那个opener，因为之前的那个opener已经包含了登录所需的cookie信息
req = request.Request(dapeng_url, headers=headers)

resp = opener.open(req)
with open('renren.html', 'w', encoding='utf-8') as fp:
    fp.write(resp.read().decode('utf-8'))
