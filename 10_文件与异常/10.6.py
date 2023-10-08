user01 = input("请输入第一个数字：")
user02 = input("请输入第二个数字：")
try:
    result = int(user01) + int(user02)
except ValueError:
    print("请输入合理的数字")

else:
    print(result)


