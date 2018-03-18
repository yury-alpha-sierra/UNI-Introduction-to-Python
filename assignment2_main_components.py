"""[summary]

"""

from modules import Application


POSTAGE_SERVICE = Application(
    'Postage Service', './/data//', 'Countries and Zones.csv')
POSTAGE_SERVICE.country = 'China'
POSTAGE_SERVICE.weight = 1132

with POSTAGE_SERVICE as p:

    p.get_available_serice_price_options()