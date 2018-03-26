"""[summary]

"""
from application import Application


POSTAGE_SERVICE = Application(
    'Postage Service', './/data//', 'Countries and Zones.csv',
    'sales_history.csv')

# sales_num = 2043  #2046
# s_history = ()

# s_history = p.get_sales_history_by_sales_number(sales_num)

# if not POSTAGE_SERVICE.single_row:
#     for each_item in s_history:
#         date_time, type, weight, destination, postage_method, quantity, cost = each_item
#         print('{}  {}  {}  {}  {}  {}  {}  {}'.format(sales_num, date_time, type, weight, destination, postage_method, quantity, cost))
# else:
#     date_time, type, weight, destination, postage_method, quantity, cost = s_history
#     print('{}  {}  {}  {}  {}  {}  {}  {}'.format(sales_num, date_time, type, weight, destination, postage_method, quantity, cost))
