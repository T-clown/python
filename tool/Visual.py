# -*- coding: UTF-8 -*-
"""
@File    ：得分.py
@Author  ：叶庭云
@CSDN    ：https://yetingyun.blog.csdn.net/
"""
import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.datasets import register_files
from pyecharts.globals import CurrentConfig

# 导入自定义的主题 可自己定制  也可以就用pyecharts官方的几种
register_files({"myTheme": ["themes/myTheme", "js"]})
CurrentConfig.ONLINE_HOST = 'D:/python/pyecharts-assets-master/assets/'

df = pd.read_excel('datas.xlsx')
up_score = list(df['up_score'])
down_score = list(df['down_score'])
x_data = [i for i in range(1, 101)]

c = (
    Line(init_opts=opts.InitOpts(theme='myTheme'))
        .add_xaxis(xaxis_data=x_data)
        .set_colors(['#7FFF00', 'red'])  # 设置两条折线图的颜色
        .add_yaxis('up_score', y_axis=up_score,
                   label_opts=opts.LabelOpts(is_show=False)
                   )
        .add_yaxis('down_socre', y_axis=down_score,
                   label_opts=opts.LabelOpts(is_show=False)
                   )
        .set_global_opts(  # 设置x轴 y轴标签
        xaxis_opts=opts.AxisOpts(name='排名'),
        yaxis_opts=opts.AxisOpts(name='得分'),
        title_opts=opts.TitleOpts('得分情况')

    )
        .render('得分.html')
)
