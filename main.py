# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# 3.1
names = ["杨向宇", "向", "虞", "基"]
greetings = "SB是"
print(greetings + names[0])

# 3.4
names = ["杨向宇", "向", "虞", "基"]
invite = "在吃翔"
print(names[0] + invite)

# 3.5
names = ["杨向宇", "向", "虞", "基"]
invite = "在吃翔"
print(names[3] + "不能来了")
names[3] = "李"
print(names[0] + invite)
print(names[1] + invite)
print(names[2] + invite)
print(names[3] + invite)

# 3.6
names = ["杨向宇", "向", "虞", "基"]
invite = "一起吃饭"
print(names[0] + invite)
print("有了更大的餐桌")
names.insert(0, "小刘")
names.insert(3, "小张")
names.append("小习")
print(names[0] + invite)
print(names[1] + invite)
print(names[2] + invite)
print(names[3] + invite)
print(names[4] + invite)
print(names[5] + invite)

# 3.8
Destin = ["Swizerland", "Xinjia", "Xizang", "Zibo", "Australia"]

print(Destin)
print("\n")

print(sorted(Destin))
print(Destin)
print("\n")

print(sorted(Destin, reverse=True))
print("\n")

Destin.reverse()
print(Destin)
print("\n")

Destin.reverse()
print(Destin)
print("\n")

Destin.sort()
print(Destin)
print("\n")

Destin.sort(reverse=True)
print(Destin)
print("\n")

c = len(Destin)
print(c)
