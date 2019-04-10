# -*- coding:utf-8 -*-
'''
@author:coyote
@datetime:2019/4/9 23:04
@file: demo12_xpath.py
@function:
使用方式：
使用//获取整个页面当中的元素，然后写标签名，然后再写谓词进行提取，比如：
//div[@class='abc']

1 /和//的区别：/代表值获取直接子节点，//获取子孙节点，一般//用得比较多
2 contains：有时候某个属性中包含了多个值，那么可以使用‘contains’函数，示例代码如下：
//div[contains(@class,'job_detail')]
3 谓词中的下标是从1开始的，不是从0开始的

'''

"""
使用lxml解析HTML代码
1.解析HTML字符串，使用lxml.etree.HTML进行解析
2.解析HTML文件，使用lxml.etree.parse进行解析
    这个函数默认使用XML解析器，所以如果碰到一些不规范的HTML代码的时候，就会解析错误
    这时候就要自己创建HTML解析器"""
from lxml import etree

text = """
<div class="left" id="home_ll">
    <div id="hworkplace">
        <a href="position.php">全部</a>
        <a href="position.php?lid=2218">深圳</a>
        <a href="position.php?lid=2156">北京</a>
        <a href="position.php?lid=2175">上海</a>
        <a href="position.php?lid=2196">广州</a>
        <a href="position.php?lid=2268">成都</a>
        <a href="position.php?lid=2459">香港</a>
        <a href="position.php?lid=2426">昆明</a>
        <a href="position.php?lid=33">美国</a>
        <a href="position.php?lid=2355">武汉</a>
    </div>
    <div id="hzhiwei">
        <a href="position.php">全部</a>
        <a href="position.php?tid=87">技术类</a>
        <a href="position.php?tid=82">产品/项目类</a>
        <a href="position.php?tid=83">市场类</a>
        <a href="position.php?tid=81">设计类</a>
        <a href="position.php?tid=84">职能类</a>
        <a href="position.php?tid=85">内容编辑类</a>
        <a href="position.php?tid=86">客户服务类</a>
    </div>
</div>
"""


def parse_text():
    htmlElement = etree.HTML(text)
    # print(type(htmlElement))
    print(etree.tostring(htmlElement, encoding='utf-8').decode('utf-8'))


def parse_tencent_file():
    htmlElement = etree.parse('tencent.html')
    # print(type(htmlElement))
    print(etree.tostring(htmlElement, encoding='utf-8').decode('utf-8'))


def parse_lagou_file():
    parser = etree.HTMLParser(encoding='utf-8')
    htmlElement = etree.parse('lagou.html', parser=parser)
    # print(type(htmlElement))
    print(etree.tostring(htmlElement, encoding='utf-8').decode('utf-8'))


if __name__ == '__main__':
    # parse_tencent_file()
    parse_lagou_file()
