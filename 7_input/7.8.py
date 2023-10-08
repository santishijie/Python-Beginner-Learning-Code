sandwich_orders = ['apple', 'tomato', 'beaf','pastrami']
finished_sandwich = []
# while sandwich_orders:
#     sandwich = sandwich_orders.pop()
#     print("I made your " + sandwich + ' sandwith')
#     finished_sandwich.append(sandwich)
# print("finished_sandwich:")
# for i in finished_sandwich:
#     print(i)

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
for i in sandwich_orders:
    print(i)


