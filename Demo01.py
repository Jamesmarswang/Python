# coding = utf-8
# __author__ = 'wang wei'


"""
import numpy as np
import time
import math


a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
c = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10]])

print(a)
print(b)
print(c)
print("==============")
print(a.shape)
print(b.shape)
print(c.shape)

print(np.logspace(0, 2, 20))


x = [i * 0.001 for i in range(10000)]
start = time.clock()
for i, t in enumerate(x):
    x[i] = math.sin(t)
print(time.clock() - start)

x = [i * 0.001 for i in range(10000)]
x = np.array(x)
start = time.clock()
np.sin(x, x)
print(time.clock() - start)"""

import math
from pylab import *
import numpy as np

if __name__ == '__main__':
    """
        x = [float(i) / 100.0 for i in range(1, 300)]
        y = [math.log(i) for i in x]
        plt.plot(x, y, 'r-', linewidth=3, label='log Curve')
        a = [x[20], x[175]]
        b = [y[20], y[175]]
        plt.plot(a, b, 'g-', linewidth=2)
        plt.plot(a, b, 'b*', markersize=15, alpha=0.75)
        plt.legend(loc='upper left')
        plt.grid(True)
        plt.xlabel('X')
        plt.ylabel('log(X)')
        plt.show()
        print("运行完成！！")
    ######################################
    u = numpy.random.uniform(0.0, 1.0, 10000)
    plt.hist(u, 80, facecolor='g', alpha=0.75)
    plt.grid(True)
    plt.show()

    times = 10000
    for time in range(times):
        u += numpy.random.uniform(0.0, 1.0, 10000)

    print(len(u))
    u /= times
    print(len(u))
    plt.hist(u, 80, facecolor='g', alpha=0.75)
    plt.grid(True)
    plt.show()"""

    x = np.arange(0.05, 3, 0.05)
    y1 = [math.log(a, 1.5) for a in x]
    plt.plot(x, y1, linewidth=2, color='#007500', label='log1.5(x)')
    plt.plot([1, 1], [y1[0], y1[-1]], 'r--', linewidth=2)
    y2 = [math.log(a, 2) for a in x]
    plt.plot(x, y2, linewidth=2, color='#9F35FF', label='log2(x)')
    y3 = [math.log(a, 3) for a in x]
    plt.plot(x, y3, linewidth=2, color='#F75000', label='log3(x)')
    plt.legend(loc='lower right')
    plt.grid(True)
    plt.show()
    print("=====显示完成==========")


X = np.linspace(-np.pi, np.pi, 256, endpoint=True)

# 创建一个8*6点（point）的图，并设置分辨率为80
figure(figsize=(8, 6), dpi=80)

# 创建一个新的1*1的子图，接下来的图样绘制在其中的第一块
subplot(1, 1, 1)
X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)
# 绘制余弦曲线，使用蓝色的，连续的，宽度为1（像素）的线条
plot(X, C, color="blue", linewidth=1.0, linestyle='-')
plot(X, S, color='green', linewidth=1.0, linestyle='-')

# 设置横轴的上下限
xlim(-4.0, 4.0)

# 设置横轴记号
xticks(np.linspace(-4, 4, 9, endpoint=True))
ylim(-1.0, 1.0)
yticks(np.linspace(-1, 1, 5, endpoint=True))

# 以分辨率72来保存图片
# savefig("exercice_2.png", dpi=72)

xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi], [r'$-\pi$'])

show()


date = datetime.datetime.strptime('20161215', '%Y%m%d').strftime('%Y-%m-%d')
print(date)
y = int(date.split('-')[0])
if date.split('-')[1][0:1] == '0':
    m = int(date.split('-')[1][1:2])
else:
    m = int(date.split('-')[1])
if date.split('-')[2][0:1] == '0':
    d = int(date.split('-')[2][1:2])
else:
    d = int(date.split('-')[2])

print(m, d)

curDay = datetime.datetime(y, m, d).date()
yesterday2 = curDay - datetime.timedelta(days=1)
data_day_int_yes2 = yesterday2.strftime("%Y%m%d")
data_day_str_yes2 = yesterday2.isoformat()

print(str(curDay) + ":" + str(yesterday2) + ":" + str(data_day_int_yes2) + ":" + str(data_day_str_yes2))
firstday_month = date[0:7] + '-01'
print(firstday_month)


curDay = datetime.datetime.strptime('20161215', '%Y%m%d').strftime('%Y-%m-%d')
yesterday2 = datetime.datetime.strptime('20161214', '%Y%m%d').strftime('%Y-%m-%d')

data_day_str_yes2 = yesterday2

print(curDay)
print(yesterday2)
print(data_day_str_yes2)



import tensorflow
