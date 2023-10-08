import matplotlib.pyplot as plt

# input_values = [1, 2, 3, 4, 5]
# squares = [1, 4, 9, 16, 25]
input_values = range(1, 1001)
squares = [x ** 2 for x in input_values]
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(input_values, squares, c=squares, cmap=plt.cm.Blues, s=10)
# 设置图形标题并给坐标轴加标签
ax.set_title("Squares Number", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Squares of Value", fontsize=14)
# 设置刻度标记的样式
ax.tick_params(labelsize=12)
# 设置坐标轴的取值范围
ax.axis([0, 1100, 0, 1100000])

plt.savefig('squares_plot.png', bbox_inches='tight')
plt.show()
