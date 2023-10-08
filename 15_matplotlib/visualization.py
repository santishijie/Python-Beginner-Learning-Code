import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)
# 设置图形标题并给坐标轴加标签
ax.set_title("Squares Number", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Value", fontsize=14)
# 设置刻度标记的样式
ax.tick_params(labelsize=12)

plt.show()
