import schedule
import pandas as pd
from datetime import datetime
import requests
from bs4 import BeautifulSoup

url = "https://s.weibo.com/top/summary?cate=realtimehot&sudaref=s.weibo.com&display=0&retcode=6102"
get_info_dict = {}
count = 0


def main():
    global url, get_info_dict, count
    get_info_list = []
    print("正在爬取数据~~~")
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')
    for tr in soup.find_all(name='tr', class_=''):
        get_info = get_info_dict.copy()
        get_info['title'] = tr.find(class_='td-02').find(name='a').text
        try:
            get_info['num'] = eval(tr.find(class_='td-02').find(name='span').text)
        except AttributeError:
            get_info['num'] = None
        get_info['time'] = datetime.now().strftime("%Y/%m/%d %H:%M")
        get_info_list.append(get_info)
    get_info_list = get_info_list[1:16]
    df = pd.DataFrame(get_info_list)
    if count == 0:
        df.to_csv('datas.csv', mode='a+', index=False, encoding='gbk')
        count += 1
    else:
        df.to_csv('datas.csv', mode='a+', index=False, header=False, encoding='gbk')


# 定时爬虫
schedule.every(1).minutes.do(main)

while True:
    schedule.run_pending()
