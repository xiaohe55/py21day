# -*- coding:utf-8 -*-
'''
@author:coyote
@datetime:2019/4/9 22:15
@file: demo11_requests_cookie.py
@function:不好使了
'''
import requests

# response = requests.get("http://www.baidu.com")
# print(response.cookies)
# print(response.cookies.get_dict())

url = "http://www.renren.com/ajax/ShowCaptcha"
data = {
    "email": 'zhuzhanji1',
    "password": "881106"
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}
session = requests.Session()
session.post(url, data=data, headers=headers)
response = session.get('http://www.renren.com/880151247/profile')
with open("renren.html", 'w', encoding='utf-8') as fp:
    fp.write(response.text)
