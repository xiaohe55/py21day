# -*- coding:utf-8 -*-
'''
@author:coyote
@datetime:2019/4/8 23:09
@file: demo9_requests_post.py
@function:已经被封
如果返回的是json数据，可以调用response.json()，将json字符串转换为字典或者列表
'''
import requests

data = {
    'first': 'true',
    'pn': '1',
    'kd': 'python'
}

headers = {
    'Cookie': '_ga=GA1.2.922025169.1527862317; user_trace_token=20180601221158-bf4948b4-65a5-11e8-934e-5254005c3644; LGUID=20180601221158-bf494e87-65a5-11e8-934e-5254005c3644; _gid=GA1.2.956660846.1554736093; LGSID=20190408230813-2142da79-5a10-11e9-8cd6-5254005c3644; PRE_UTM=; PRE_HOST=www.google.com; PRE_SITE=https%3A%2F%2Fwww.google.com%2F; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; index_location_city=%E6%B7%B1%E5%9C%B3; JSESSIONID=ABAAABAAAGGABCBE500C1662858C1F548A66F71373B218B; X_HTTP_TOKEN=6c5bd9460796d27d0186374551f9f2a0c3bee758b1; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1554736094,1554736811; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1554736811; _gat=1; LGRID=20190408232010-ccbb404f-5a11-11e9-9ca6-525400f775ce; TG-TRACK-CODE=index_search; SEARCH_ID=e1580efa0c6f4c48a52c0586e32b8103',
    'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}
response = requests.post(
    'http://www.lagou.com/jobs/positionAjax.json?city=%E6%B7%B1%E5%9C%B3&needAddtionalResult=false',
    data=data, headers=headers)

print(response.json())
