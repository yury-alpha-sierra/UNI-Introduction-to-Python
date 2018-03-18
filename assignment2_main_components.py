"""[summary]

Returns:
    [type] -- [description]
"""

from postal_app.application import Application



POSTAGE_SERVICE = Application(
    'Postage Service', './/data//', 'Countries and Zones.csv')
POSTAGE_SERVICE.country = 'China'
POSTAGE_SERVICE.weight = 1132

POSTAGE_SERVICE.register_service(
    'Economy Letter', 'Economy Letters Price Guide ($).csv')
POSTAGE_SERVICE.register_service(
    'Economy Parcel by Air', 'Economy Parcel Price Guide_by Air ($).csv')
POSTAGE_SERVICE.register_service(
    'Economy Parcel by Sea', 'Economy Parcel Price Guide_by Sea ($).csv')
POSTAGE_SERVICE.register_service(
    'Express Letter', 'Express Letter Price Guide ($).csv')
POSTAGE_SERVICE.register_service(
    'Express Parcel', 'Express Parcel Price Guide ($).csv')
POSTAGE_SERVICE.register_service(
    'Standard Parcel', 'Standard Parcel Price Guide ($).csv')

POSTAGE_SERVICE.instantiate_service()

POSTAGE_SERVICE.get_available_serice_price_options()
