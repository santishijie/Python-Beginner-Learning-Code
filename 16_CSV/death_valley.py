from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('death_valley_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)
# for index, column_header in enumerate(header_row):
#     print(index, column_header)

# 提取最高温度和日期
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high = int(row[3])
        low = int(row[4])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
# print(highs)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, color=(0.8, 0.1, 0.1))
ax.plot(dates, lows, color=(0.1, 0.6, 0.3))

# 设置绘图格式
ax.set_title("Daily High and Low Temperatures, 2021\nDeath Valley", fontsize=21)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperatures(F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
