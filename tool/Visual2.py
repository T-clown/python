# -*- coding: UTF-8 -*-
"""
@File    ：女神地区.py
@Author  ：叶庭云
@CSDN    ：https://yetingyun.blog.csdn.net/
"""
import pandas as pd
from collections import Counter
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType, CurrentConfig
import random

CurrentConfig.ONLINE_HOST = 'D:/python/pyecharts-assets-master/assets/'

df = pd.read_excel('datas.xlsx')
areas = df['country']
area_list = []
for item in areas:
    if '-' in item:
        item = item.split('-')
        for i in item:
            area_list.append(i)
    else:
        area_list.append(item)

area_count = Counter(area_list).most_common(10)
print(area_count)
area = [x[0] for x in area_count]
nums = [y[1] for y in area_count]
# 使用风格
bar = Bar(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
colors = ['red', '#0000CD', '#000000', '#008000', '#FF1493', '#FFD700', '#FF4500', '#00FA9A', '#191970', '#9932CC']
random.shuffle(colors)
# 配置y轴数据  Baritem
y = []
for i in range(10):
    y.append(
        opts.BarItem(
            name=area[i],
            value=nums[i],
            itemstyle_opts=opts.ItemStyleOpts(color=colors[i])  # 设置每根柱子的颜色
        )
    )
bar.add_xaxis(xaxis_data=area)
bar.add_yaxis("上榜美女数", y)
bar.set_global_opts(xaxis_opts=opts.AxisOpts(
    name='国家',
    axislabel_opts=opts.LabelOpts(rotate=45)
),
    yaxis_opts=opts.AxisOpts(
        name='上榜美女数', min_=0, max_=55,  # y轴刻度的最小值 最大值
    ),
    title_opts=opts.TitleOpts(
        title="各地区上榜美女数",
        title_textstyle_opts=opts.TextStyleOpts(
            font_family="KaiTi", font_size=25, color="black"
        )
    ))
# 标记最大值  最小值  平均值   标记平均线
bar.set_series_opts(label_opts=opts.LabelOpts(is_show=False),
                    markpoint_opts=opts.MarkPointOpts(
                        data=[
                            opts.MarkPointItem(type_="max", name="最大值"),
                            opts.MarkPointItem(type_="min", name="最小值"),
                            opts.MarkPointItem(type_="average", name="平均值")]),
                    markline_opts=opts.MarkLineOpts(
                        data=[
                            opts.MarkLineItem(type_="average", name="平均值")]))
bar.render("女神地区分布.html")
