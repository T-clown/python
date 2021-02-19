"""
https://mp.weixin.qq.com/s/LsrXRPuKrbEEjV5sC9rmEQ
"""
import requests
import logging
from fake_useragent import UserAgent
from lxml import etree

# 日志输出的基本配置
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
# 随机产生请求头
ua = UserAgent(verify_ssl=False, path='fake_useragent.json', use_cache_server=False)
url = 'https://www.zhongnongwang.com/quote/product-htm-page-1.html'
# 伪装请求头
headers = {
    "Accept-Encoding": "gzip",  # 使用gzip压缩传输数据让访问更快
    "User-Agent": ua.random
}
# 发送请求  获取响应

rep = requests.get(url, headers=headers)
# print(rep.status_code)    # 200
# Xpath定位提取数据
html = etree.HTML(rep.text)
items = html.xpath('/html/body/div[10]/table/tr[@align="center"]')
logging.info(f'该页有多少条信息：{len(items)}')  # 一页有20条信息
# 遍历提取出数据
for item in items:
    name = ''.join(item.xpath('.//td[1]/a/text()'))  # 品名
    price = ''.join(item.xpath('.//td[3]/text()'))  # 最新报价
    unit = ''.join(item.xpath('.//td[4]/text()'))  # 单位
    nums = ''.join(item.xpath('.//td[5]/text()'))  # 报价数
    time_ = ''.join(item.xpath('.//td[6]/text()'))  # 报价时间
    logging.info([name, price, unit, nums, time_])
