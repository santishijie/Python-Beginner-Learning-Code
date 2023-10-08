# print("hello,world")
# money = 50
# str_money = str(money)
# print("30+20=", money)
# print("要加油啊")
# print("给自己一个平凡的生活")
# print("hello,world "+ str_money +" hello,new person")
# print(f"2*3 = {1 * 6}")
# name = "好好活着"
# stock_price = 19.99
# stock_code = "414400"
# stock_price_growth = 1.2
# growth = 7
# finally_price = stock_price * stock_price_growth ** growth
# print(f"name:{name},code:{stock_code}")
# print("每日增长因子：%.1f,经过%d天的增长后达到：%.2f" % (stock_price_growth, growth, finally_price))
# user_name = input("你好： ")
# user_type = input("你是尊贵的：")
# print(f"{user_name} {user_type} "+ "用户")
# num1 = 10
# num2 = 5
# print(f"10>5 {num1 == num2}")
# age = int(input())
# if age > 18:
#     print("该赚钱了")
# else:
#     print("还可休息一下")
# name = "simple"
# for x in name:
#     print(x)
# money = 500000
# name = None
# name = input("请输入你的姓名：")
#
# def query(show_header):
#     if show_header:
#         print("----查询余额----")
#     print(f"{name},你好，余额还剩：{money}元")
#
# def saving(num):
#     global money
#     money += num
#     print("------存款--------")
#     print(f"{name},你好，你存款{num}元成功")
#     query(False)
#
# def get_money(num):
#     global money
#     money -= num
#     print("------取款--------")
#     if money > 0:
#         print(f"{name},你好，你取款{num}元成功")
#         query(False)
#     else:
#         print("余额不足")
#
#
# def main():
#     print("------主菜单--------")
#     print(f"{name}，你好，欢迎来到银行")
#     print("查询余额\t[输入1]")
#     print("存款\t\t[输入2]")
#     print("取款\t\t[输入3]")
#     print("退出\t\t[输入4]")
#     return input("输入你的选择：")
#
# while True:
#     keyword_input = main()
#     if keyword_input == '1':
#         query(True)
#         continue
#
#     elif keyword_input == '2':
#         num = int(input("你存多少钱？请输入："))
#         saving(num)
#         continue
#
#     elif keyword_input == '3':
#         num = int(input("你存多少钱？请输入："))
#         get_money(num)
#         continue
#
#     else:
#         print("退出")
#         break

# my_list = ["jack","Tom","Rose"]
# print(my_list[0])
# print(my_list[2])
# print(my_list[1])
# t1 = (1,"hello",True)
# t2 = tuple()
# t3 = ("world",)
# print(f"{t1}")
# print(f"{t2}")

def test_return():
    return 1, 2


x, y = test_return()
print(x, y)
