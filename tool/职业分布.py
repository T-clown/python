# -*- coding: UTF-8 -*-
"""
https://yetingyun.blog.csdn.net/
"""
import pandas as pd
from collections import Counter
from pyecharts.charts import Pie
from pyecharts import options as opts
from pyecharts.globals import ThemeType, CurrentConfig

# 引用本地js资源渲染
CurrentConfig.ONLINE_HOST = 'D:/python/pyecharts-assets-master/assets/'

df = pd.read_excel('datas.xlsx')
data = list(df['occupation'])
job_count = Counter(data).most_common()

pie = Pie(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
# 富文本效果  环图
pie.add('职业', data_pair=job_count, radius=["40%", "55%"],
        label_opts=opts.LabelOpts(
            position="outside",
            formatter="{a|{a}}{abg|}\n{hr|}\n {b|{b}: }{c}  {per|{d}%}  ",
            background_color="#eee",
            border_color="#aaa",
            border_width=1,
            border_radius=4,
            rich={
                "a": {"color": "#999", "lineHeight": 22, "align": "center"},
                "abg": {
                    "backgroundColor": "#e3e3e3",
                    "width": "100%",
                    "align": "right",
                    "height": 22,
                    "borderRadius": [4, 4, 0, 0],
                },
                "hr": {
                    "borderColor": "#aaa",
                    "width": "100%",
                    "borderWidth": 0.5,
                    "height": 0,
                },
                "b": {"fontSize": 16, "lineHeight": 33},
                "per": {
                    "color": "#eee",
                    "backgroundColor": "#334455",
                    "padding": [2, 4],
                    "borderRadius": 2,
                },
            },
        ), )
pie.set_global_opts(title_opts=opts.TitleOpts(title='职业占比'))
pie.set_colors(['red', 'orange', 'purple'])  # 设置颜色
pie.render('美女职业分布.html')
