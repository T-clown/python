# coding: utf8

"""整站爬虫"""
from urllib.parse import urljoin

from gevent import monkey

monkey.patch_all()

import requests
from lxml import etree
from gevent.pool import Pool
from gevent.queue import Queue

base_url = 'https://book.douban.com'

# 种子URL
start_url = 'https://book.douban.com/tag/?view=type&icn=index-sorttags-all'

# 解析规则
rules = {
    # 标签页列表
    'list_urls': "//table[@class='tagCol']/tbody/tr/td/a/@href",
    # 详情页列表
    'detail_urls': "//li[@class='subject-item']/div[@class='info']/h2/a/@href",
    # 页码
    'page_urls': "//div[@id='subject_list']/div[@class='paginator']/a/@href",
    # 书名
    'title': "//div[@id='wrapper']/h1/span/text()",
}
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"}

# 定义队列
list_queue = Queue()
detail_queue = Queue()

# 定义协程池
pool = Pool(size=10)


def crawl(url,headers):
    """首页"""
    response = requests.get(url,headers=headers)
    list_urls = etree.HTML(response.text).xpath(rules['list_urls'])
    for list_url in list_urls:
        list_queue.put(urljoin(base_url, list_url))


def list_loop():
    """采集列表页"""
    while True:
        list_url = list_queue.get()
        pool.spawn(crawl_list_page, list_url, headers)


def detail_loop():
    """采集详情页"""
    while True:
        detail_url = detail_queue.get()
        pool.spawn(crawl_detail_page, detail_url, headers)


def crawl_list_page(list_url, headers):
    """采集列表页"""
    html = requests.get(list_url, headers=headers).text
    detail_urls = etree.HTML(html).xpath(rules['detail_urls'])
    # 详情页
    for detail_url in detail_urls:
        detail_queue.put(urljoin(base_url, detail_url))

    # 下一页
    list_urls = etree.HTML(html).xpath(rules['page_urls'])
    for list_url in list_urls:
        list_queue.put(urljoin(base_url, list_url))


def crawl_detail_page(list_url, headers):
    """采集详情页"""
    html = requests.get(list_url, headers=headers).text
    title = etree.HTML(html).xpath(rules['title'])[0]
    print(title)


def main():
    # 1. 标签页
    crawl(start_url,headers)
    # 2. 列表页
    pool.spawn(list_loop)
    # 3. 详情页
    pool.spawn(detail_loop)
    # 开始采集
    pool.join()


if __name__ == '__main__':
    main()
