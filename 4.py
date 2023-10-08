# 4.1
lists = ["mango", "durian", "pineapple"]
for list in lists:
    print(list)
    print("I like " + list + " pizza")
print("I really love this pizza!")

# 4.4
number = []
for i in range(1, 1000001):
    number.append(i)
# for i in number:
#     print(i)
min = min(number)
print(min)
sum = sum(number)
print(sum)

# 4.8
a = []
b = range(1, 11)
for i in b:
    a.append(i**3)
print(a)

# 4.9
c = [i**3 for i in range(1, 11)]
print(c)

# 4.10
d = [i for i in range(1, 11)]
# d = range(1, 11)
print(d[0:3])
print(d[3:7])

# 4.11
friend_pizzas = lists[:]
lists.append("草莓芝士")
friend_pizzas.append("榴莲芝士")
print("My favorite pizzas are:")
print(lists)
print("My friend's favorite pizzas are:")
print(friend_pizzas)

# 4.13
foods = ('烤肉', '火锅', '猪脚饭', '卤菜', '鸡公煲')
for i in foods:
    print(i)
# foods.append('酸菜鱼')
foods = ('烤肉', '火锅', '猪脚饭', '肯德基', '麦当劳')
for i in foods:
    print(i)