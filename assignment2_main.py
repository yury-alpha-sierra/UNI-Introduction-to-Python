"""[summary]

"""


import pandas as pd

from modules import Application

sales_history = {}
def __import_sales_history():


    try:
        return_dictionary = pd.read_csv(
            POSTAGE_SERVICE.data_base_directory + POSTAGE_SERVICE.sales_history_file, header=0, index_col=0,
            squeeze=True)
    except FileNotFoundError:
        print('File "{}" could not be found. Please, make sure it exists and you have rights to read it.\nProgram will terminate now.'.format(  # pylint: disable=C0301
            POSTAGE_SERVICE.sales_history_file))
        exit(404)
    return return_dictionary


POSTAGE_SERVICE = Application('Postage Service', './/data//', 'Countries and Zones.csv', 'sales_history.csv')
POSTAGE_SERVICE.country = 'China'
POSTAGE_SERVICE.weight = 1132

with POSTAGE_SERVICE as p:

    p.get_available_serice_price_options()

sales_history = __import_sales_history()
# print(sales_history[sales_history.columns[1]])
print(sales_history.loc[1])
# print(max(sales_history.index))
