import requests;
import bs4

mylist = []
r = requests.get(url='https://s.weibo.com/top/summary?Refer=top_hot&topnav=1&wvr=6', timeout=10)
print(r.status_code)  # 获取返回状态
r.encoding = r.apparent_encoding
demo = r.text
from bs4 import BeautifulSoup

soup = BeautifulSoup(demo, "html.parser")
for link in soup.find('tbody'):
    hotnumber = ''
    if isinstance(link, bs4.element.Tag):
        #  print(link('td'))
        lis = link('td')
        hotrank = lis[1]('a')[0].string  # 热搜排名
        hotname = lis[1].find('span')  # 热搜名称
        if isinstance(hotname, bs4.element.Tag):
            hotnumber = hotname.string  # 热搜指数
            pass
        mylist.append([lis[0].string, hotrank, hotnumber, lis[2].string])
f = open("/Users/hrtps/Desktop/hotsearch.txt", "w+")
for line in mylist:
    f.write('%s %s %s %s\n' % (line[0], line[1], line[2], line[3]))
