import os
import matplotlib.pyplot as plt
import imageio
import numpy as np

coordinates_lists = [[[0], [0]],
                     [[100, 200, 300], [100, 200, 300]],
                     [[400, 500, 600], [400, 500, 600]],
                     [[400, 500, 600, 400, 500, 600], [400, 500, 600, 600, 500, 400]],
                     [[500], [500]],
                     [[0], [0]]]
gif_name = 'movie'
n_frames = 10
bg_color = '#95A4AD'
marker_color = '#283F4E'
marker_size = 25
print('生成图表\n')
filenames = []
for index in np.arange(0, len(coordinates_lists) - 1):
    # 获取当前图像及下一图像的x与y轴坐标值
    x = coordinates_lists[index][0]
    y = coordinates_lists[index][1]
    x1 = coordinates_lists[index + 1][0]
    y1 = coordinates_lists[index + 1][1]
    # 查看两点差值
    while len(x) < len(x1):
        diff = len(x1) - len(x)
        x = x + x[:diff]
        y = y + y[:diff]
    while len(x1) < len(x):
        diff = len(x) - len(x1)
        x1 = x1 + x1[:diff]
        y1 = y1 + y1[:diff]
    # 计算路径
    x_path = np.array(x1) - np.array(x)
    y_path = np.array(y1) - np.array(y)
    for i in np.arange(0, n_frames + 1):
        # 计算当前位置
        x_temp = (x + (x_path / n_frames) * i)
        y_temp = (y + (y_path / n_frames) * i)
        # 绘制图表
        fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(aspect="equal"))
        ax.set_facecolor(bg_color)

        plt.scatter(x_temp, y_temp, c=marker_color, s=marker_size)
        plt.xlim(0, 1000)
        plt.ylim(0, 1000)
        # 移除边框线
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        # 网格线
        ax.set_axisbelow(True)
        ax.yaxis.grid(color='gray', linestyle='dashed', alpha=0.7)
        ax.xaxis.grid(color='gray', linestyle='dashed', alpha=0.7)
        # 保存图片
        filename = f'images/frame_{index}_{i}.png'
        filenames.append(filename)
        if (i == n_frames):
            for i in range(5):
                filenames.append(filename)
        # 保存
        plt.savefig(filename, dpi=96, facecolor=bg_color)
        plt.close()
print('保存图表\n')
# 生成GIF
print('生成GIF\n')
with imageio.get_writer(f'{gif_name}.gif', mode='I') as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)
print('保存GIF\n')
print('删除图片\n')
# 删除图片
for filename in set(filenames):
    os.remove(filename)
print('完成')
