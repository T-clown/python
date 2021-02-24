# coding: utf8

"""简单爬虫"""
"""
 requests 爬取博客园内容AttributeError: 'NoneType' object has no attribute 'xpath'
 原因是请求Get 需要增加 headers来解决反扒
"""
import requests
from lxml import etree


def main():
    # 1. 定义页面URL和解析规则
    crawl_urls = [
        'https://book.douban.com/subject/25862578/',
        'https://book.douban.com/subject/26698660/',
        'https://book.douban.com/subject/2230208/'
    ]
    parse_rule = "//div[@id='wrapper']/h1/span/text()"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"}
    for url in crawl_urls:
        # 2. 发起HTTP请求
        response = requests.get(url, headers=headers)

        # 3. 解析HTML
        result = etree.HTML(response.text).xpath(parse_rule)[0]

        # 4. 保存结果
        print(result)

if __name__ == '__main__':
    main()
