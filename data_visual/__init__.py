import imageio
import matplotlib.pyplot as plt
import numpy as np

# # 生成40个取值在30-40的数
# y = np.random.randint(30, 40, size=40)
# # 绘制折线
# plt.plot(y)
# # 设置y轴最小值和最大值
# plt.ylim(20, 50)
#
# # 显示
# plt.show()
#
#
#
# # 第一张图
# plt.plot(y[:-3])
# plt.ylim(20, 50)
# plt.savefig('1.png')
# plt.show()
#
# # 第二张图
# plt.plot(y[:-2])
# plt.ylim(20, 50)
# plt.savefig('2.png')
# plt.show()
#
# # 第三张图
# plt.plot(y[:-1])
# plt.ylim(20, 50)
# plt.savefig('3.png')
# plt.show()
#
# # 第四张图
# plt.plot(y)
# plt.ylim(20, 50)
# plt.savefig('4.png')
# plt.show()

# 生成Gif
with imageio.get_writer('mygif.gif', mode='I') as writer:
    for filename in ['1.png', '2.png', '3.png', '4.png']:
        image = imageio.imread(filename)
        writer.append_data(image)