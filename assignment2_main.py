"""[summary]

"""


from my_modules import Application

sales_history = []


def get_sales_history(sales_number):
    return_iterable = []
    for each_value in POSTAGE_SERVICE.sales_history.loc[sales_number].values:
        return_iterable.append(each_value)

    return return_iterable


POSTAGE_SERVICE = Application('Postage Service', './/data//', 'Countries and Zones.csv', 'sales_history.csv')
POSTAGE_SERVICE.country = 'China'
POSTAGE_SERVICE.weight = 1132

# with POSTAGE_SERVICE as p:
#     p.get_available_serice_price_options()
sales_num = 201
s_history = get_sales_history(sales_num)

for each_item in s_history:
    date_time, type, weight, destination, postage_method, quantity, cost = each_item
    print('{}  {}  {}  {}  {}  {}  {}  {}'.format(sales_num, date_time, type, weight, destination, postage_method, quantity, cost))