people = {'first_name': '复旦大学', 'last_name': '东京大学', 'age': '哈佛大学', 'city': 'Dream'}
print(people['age'])
print(people['city'])

numbers = {'zhao': 2, 'qian': 3, 'sun': 5, 'li': 8, 'wan': 9}
print(numbers)

python_words = {'Code layout': '代码布局', 'Whitespaces': '空格', 'ctrl alt l': '重排代码格式', 'Comments': '注释',
                'Acwing': '力扣'}
for word, explanation in python_words.items():
    print('\n' + word + ':')
    print(explanation)
