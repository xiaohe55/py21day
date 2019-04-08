# -*- coding:utf-8 -*-
'''
@author:coyote
@datetime:2019/4/8 7:41
@file: demo8_requests.py
@function:
1.发送get请求，直接调用'requests.get'
2.response.text 和 response.content 区别
1)response.content：这个是直接从网络中获取的数据，没有经过任何解码，所以是一个bytes类型，
其实在硬盘上和在网络上传输的字符串就是byte类型
2) response.text ：这个是str数据类型，是requests库将requests.content进行解码的字符串，
解码需要指定一个编码方式，requests会根据自己的猜测来判断编码的方式。所以有时候会猜测错误，
就会导致解码产生乱码。这时候就应该使用'response.content.decode('utf-8')'进行手动解码

'''
import requests

response = requests.get('http://www.baidu.com')

# print(type(response.text))
# print(response.text)

# print(type(response.content))
# print(response.content.decode('utf-8'))

# print(response.url)
# print(response.encoding)
# print(response.status_code)

params = {
    'wd': "中国"
}
headers = {
    'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}
response = requests.get("http://www.baidu.com/s", params=params, headers=headers)

with open('baidu.html', 'w', encoding='utf-8') as fp:
    fp.write(response.content.decode('utf-8'))

print(response.url)
