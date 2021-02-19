# url = "https://www.qidian.com/rank?chn=21"
# lxml/etree method

import requests
from lxml import etree


# url = "https://www.qidian.com/rank?chn=1"
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'}
#
# req = requests.get(url, headers)
# html = etree.HTML(req.text)
# items = html.xpath("//div[@class='type-list']/p/a")
# for item in items:
#     type_name = ''.join(item.xpath(".//text()"))
#     type_id = ''.join(item.xpath(".//@data-chanid"))
#     print(type_id + "-" + type_name)


# 获取小说类型列表
def get_type_dict():
    type_dict = {}
    url = "https://www.qidian.com/rank?chn=1"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'}

    req = requests.get(url, headers)
    html = etree.HTML(req.text)
    items = html.xpath("//div[@class='type-list']/p/a")
    for item in items:
        type_name = ''.join(item.xpath(".//text()"))
        type_id = ''.join(item.xpath(".//@data-chanid"))
        if (int(type_id) > 0):
            type_dict[type_id] = type_name
    return type_dict


def download(type_id):
    url = f"https://www.qidian.com/rank?chn={type_id}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'}

    req = requests.get(url, headers)
    html = etree.HTML(req.text)
    # div[contains(@class,'rank-list')]  div节点的class属性值包含rank-list
    items = html.xpath("//div[@class='rank-body']/div[1]/div[contains(@class,'rank-list')]")
    for item in items:
        type_name = ''.join(item.xpath(".//h3[@class='wrap-title lang']/text()"))
        # type_id = ''.join(item.xpath(".//@data-chanid"))
        print(type_name)


download(1)
