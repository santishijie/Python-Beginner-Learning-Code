def make_pizza(*toppings):
    for topping in toppings:
        print(f"{topping}")


make_pizza('a')
make_pizza('b', 'c', 'd')


def bulid_profile(first, last, **user_info):
    user_info['first_name'] = 'first'
    user_info['last_name'] = 'last'
    return user_info


user_profile = bulid_profile('zhenhao', 'yuan', age='18', field='50000')
print(user_profile)
