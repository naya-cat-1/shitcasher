import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为SimHei
plt.rcParams['axes.unicode_minus'] = False
# 更新数据，包括2023年前三季度
years = ['2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023(前三季度)']
financing_numbers = [3.56, 13.68, 47.98, 25.76, 11.12, 17.36, 75, 0.54]

# 计算同比增长率
growth_rates = [((financing_numbers[i] - financing_numbers[i-1]) / financing_numbers[i-1] * 100) if i != 0 else 0 for i in range(len(financing_numbers))]

# 设置matplotlib正常显示中文和负号
plt.rcParams['font.sans-serif'] = ['SimHei'] # 用黑体显示中文
plt.rcParams['axes.unicode_minus'] = False # 正常显示负号

fig, ax1 = plt.subplots()

# 绘制融资数量柱状图
color = 'tab:blue'
ax1.set_xlabel('年份')
ax1.set_ylabel('项目融资金额', color=color)
bar1 = ax1.bar(years, financing_numbers, color=color, label='项目融资金额')
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_xticklabels(years, rotation=45, ha="right")

# 实例化第二个y轴
ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('增速 (%)', color=color)
line1, = ax2.plot(years, growth_rates, color=color, marker='o', label='增速')
ax2.tick_params(axis='y', labelcolor=color)

# 添加图例
fig.legend(handles=[bar1, line1], loc='upper left', bbox_to_anchor=(0.1,0.9))

plt.title('2016—2023年区块链投融资金额及增速')
plt.tight_layout()
plt.show()
