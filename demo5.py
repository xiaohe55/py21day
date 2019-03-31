# -*- coding:utf-8 -*-
'''
@author:coyote
@datetime:2019/3/31 22:56
@file: demo5.py
@function:cookie登录
'''

from urllib import request

bili_url = "http://i.baidu.com/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    'Cookie': 'BAIDUID=E5FBFD159AB92EBE493149E758D52EAC:FG=1; BIDUPSID=E5FBFD159AB92EBE493149E758D52EAC; PSTM=1526738161; MCITY=-131%3A; __cfduid=d3f33ffb30b756df5c620e4f1bba2a4a21552801141; pgv_pvi=6190321664; cflag=13%3A3; delPer=0; H_PS_PSSID=28628_1436_21101_18559_28775_28724_28557_28697_28585_26350_28604_28627_28606; BDUSS=3otc0NrdzBwcGFJRVlGSGMzRUpESTIxWkgxSlR1WTdlWVJvMk1YY3htbUtac2hjRUFBQUFBJCQAAAAAAAAAAAEAAAD-skuSAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIrZoFyK2aBcb; PHPSESSID=79e98502fca764c9smohnnoc33; Hm_lvt_4010fd5075fcfe46a16ec4cb65e02f04=1554045329,1554045355; Hm_lpvt_4010fd5075fcfe46a16ec4cb65e02f04=1554045418'}
req = request.Request(url=bili_url, headers=headers)
resp = request.urlopen(req)
with open("baidu.html", 'w', encoding='utf-8') as fp:
    # write 函数必须写入一个str的数据类型
    # resp.read()读出来的是一个byte类型
    # byte ->decode-->str
    # str-->encode-->byte
    fp.write(resp.read().decode('utf-8'))
