# -*- coding: UTF-8 -*-
"""
https://yetingyun.blog.csdn.net/
"""
import requests
from lxml import etree
import logging
from fake_useragent import UserAgent
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet.append(['ranking', 'name', 'country', 'occupation', 'up_score', 'down_score'])
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
# 随机产生请求头
ua = UserAgent(verify_ssl=False, path='fake_useragent.json')

headers = {
    "accept-encoding": "gzip",
    "upgrade-insecure-requests": "1",
    "user-agent": ua.random,
}

url = "https://kingchoice.me/topic-the-100-most-beautiful-women-in-the-world-2020-close-jan-29-2021-1255.html?option=40924"
response = requests.get(url, headers=headers)
# print(response.status_code)
# print(response.text)
html = etree.HTML(response.text)
lis = html.xpath('//div[@class="channel-box3-body box3-body"]/ul/li')
logging.info(len(lis))  # 100条信息

for index_, li in enumerate(lis, start=1):
    src = li.xpath('.//div[@class="avatar"]/img/@src')[0]  # 图片
    name = li.xpath('.//div[@class="info"]/a/h3/text()')[0]  # 姓名
    country, occupation = li.xpath('.//div[@class="info"]/span/text()')[0].split(' ', 1)  # 地区 职业
    up_score = li.xpath('.//div[@class="des"]/div[1]/ul/li[1]/span/text()')[0]  # up分数
    down_score = li.xpath('.//div[@class="des"]/div[1]/ul/li[2]/span/text()')[0]  # down分数
    img = requests.get(src, headers=headers).content
    with open(r'.\Top100_beauty_img\{}.jpg'.format(name), 'wb') as f:
        f.write(img)
    sheet.append([index_, name, country, occupation, up_score, down_score])
    logging.info([index_, name, country, occupation, up_score, down_score])
    logging.info('已保存{}的信息'.format(name))

wb.save(filename='datas.xlsx')
