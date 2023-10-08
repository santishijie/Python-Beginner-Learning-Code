import sys

sys.path.append("D:\file\pycharm\python-3RDEDITION")

import Rest

r = Rest.Restaurant('麻辣烫', '卤菜')
r.describe_restaurant()
r.open_restaurant()


