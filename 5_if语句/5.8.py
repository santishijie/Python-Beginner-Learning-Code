persons = ['mao', 'hua', 'deng', 'zhao', 'bao']
for i in persons:
    print('你好' + i)
    if i == 'bao':
        print('bao is SB')

names = []
if names:
    for i in persons:
        print('你好' + i)
        if i == 'bao':
            print('bao is SB')
else:
    print('We need to find some users')

point = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in point:
    if i == 1:
        print(i.__str__() + 'st')
    elif i == 2:
        print(i.__str__() + 'nd')
    elif i == 3:
        print(i.__str__() + 'rd')
    else:
        print(i.__str__() + 'th')
