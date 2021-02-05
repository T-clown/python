# coding: utf8

"""协程版本爬虫，提高抓取效率"""

from gevent import monkey

monkey.patch_all()

import requests
from lxml import etree
from gevent.pool import Pool


def main():
    # 1. 定义页面URL和解析规则
    crawl_urls = [
        'https://book.douban.com/subject/25862578/',
        'https://book.douban.com/subject/26698660/',
        'https://book.douban.com/subject/2230208/'
    ]
    rule = "//div[@id='wrapper']/h1/span/text()"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"}
    # 2. 抓取
    pool = Pool(size=10)
    for url in crawl_urls:
        pool.spawn(crawl, url, rule, headers)

    pool.join()


def crawl(url, rule, headers):
    # 3. 发起HTTP请求
    response = requests.get(url, headers=headers)

    # 4. 解析HTML
    result = etree.HTML(response.text).xpath(rule)[0]

    # 5. 保存结果
    print(result)


if __name__ == '__main__':
    main()
