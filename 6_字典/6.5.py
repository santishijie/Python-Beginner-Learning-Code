rivers = {'nile': 'egypt', 'Yangtze River': 'Republic of China', 'the Mississippi': 'American', 'Rhine River': 'German'}
for river, country in rivers.items():
    print("The " + river + ' runs through ' + country)
    print(river)
    print(country)

# 6.7
people = {'first_name': '复旦大学', 'last_name': '东京大学', 'age': '哈佛大学', 'city': 'Dream'}
cake = {'durian': 'expensive', 'eggs': 'two', 'cake': '沸羊羊之恋'}
fruit = {'Apple': 'melons', 'watermelon': 'melon', 'pear': 'peach'}
lists = [people, cake, fruit]
for list in lists:
    for i, j in list.items():
        print(i + ':' + j)
# 6.8
cat01 = {'type': '橘猫', 'master': 'yuan'}
cat02 = {'type': '白猫', 'master': 'zhen'}
cat03 = {'type': '黑猫', 'master': 'hao'}
pets = [cat01, cat02, cat03]
for pet in pets:
    for i, j in pet.items():
        print(i + ':' + j)

# 6.9
favorite_places = {'wang': ['交大', '电大', '工大'], 'ying': ['长大', '西工', '大皮院'],
                   'li': ['回民街', '南门街', '城墙']}
for people, places in favorite_places.items():
    print(people + '喜欢的地方:')
    for place in places:
        print(place)

# 6.11
San_Francisco = {'country': 'American', 'population': '200000', 'fact': 'The second largest city in California'}
Toronto = {'country': 'Canada', 'population': '150000', 'fact': 'The largest city in Canada'}
Frankfurt = {'country': 'German', 'population': '200000', 'fact': 'The fifth largest city in German'}
cities = {
    'San_Francisco': {'country': 'American', 'population': '200000', 'fact': 'The second largest city in California'},
    'Toronto': {'country': 'Canada', 'population': '150000', 'fact': 'The largest city in Canada'},
    'Frankfurt': {'country': 'German', 'population': '200000', 'fact': 'The fifth largest city in German'}}
for city, infos in cities.items():
    print(city + '有以下特征:')
    for i, j in infos.items():
        print(i + ':' + j)
