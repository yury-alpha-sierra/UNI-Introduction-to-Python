"""[summary]

"""
from my_modules.application import Application



POSTAGE_SERVICE = Application('Postage Service', './/data//', 'Countries and Zones.csv', 'sales_history.csv')
POSTAGE_SERVICE.country = 'China'
POSTAGE_SERVICE.weight = 1132

sales_num = 2043  #2046
s_history = ()


with POSTAGE_SERVICE as p:
    p.get_available_serice_price_options()
    s_history = p.get_sales_history_by_sales_number(sales_num)

    if not POSTAGE_SERVICE.single_row:
        for each_item in s_history:
            date_time, type, weight, destination, postage_method, quantity, cost = each_item
            print('{}  {}  {}  {}  {}  {}  {}  {}'.format(sales_num, date_time, type, weight, destination, postage_method, quantity, cost))
    else:
        date_time, type, weight, destination, postage_method, quantity, cost = s_history
        print('{}  {}  {}  {}  {}  {}  {}  {}'.format(sales_num, date_time, type, weight, destination, postage_method, quantity, cost))
