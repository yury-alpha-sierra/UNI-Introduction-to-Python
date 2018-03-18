"""[summary]

Returns:
    [type] -- [description]
"""


import re
import pandas as pd

from postal_app.service import Service

class Application:
    """[summary]
    """

    def __init__(self, name, data_dir, file_name):
        """[summary]

        Arguments:
            name {[type]} -- [description]
            data_dir {[type]} -- [description]
        """

        self.name = name
        self.services_collection = []
        self.service_name_collection = {}
        self.data_base_directory = data_dir
        self.country = ''
        self.weight = 0
        self.country_and_zone_data = {}
        self.country_file = file_name

        self.country_and_zone_data = self.__import_country_and_zone_data()

    def register_service(self, service_name, data_file):
        """[summary]

        Arguments:
            name {[type]} -- [description]
            file {[type]} -- [description]
        """

        self.service_name_collection[service_name] = data_file

    def instantiate_service(self):
        """[summary]
        """

        for each_service in self.service_name_collection:
            service = Service(
                each_service, self.data_base_directory,
                self.service_name_collection.get(each_service))
            service.application = self
            self.services_collection.append(service)

    def get_available_serice_price_options(self):
        """[summary]
        """

        for each_service in self.services_collection:
            print('{} --> {}'.format(each_service.get_service_name(),
                                     each_service.get_service_price(self.country, self.weight)))

    def __import_country_and_zone_data(self):
        """[summary]

        Returns:
            [type] -- [description]
        """

        return_dictionary = {}
        try:
            with open(self.data_base_directory + self.country_file) as csv_file:
                next(csv_file)
                for each_line in csv_file.readlines():
                    each_line = each_line.split(',')
                    return_dictionary[each_line[0]] = each_line[1]
        except FileNotFoundError:
            print('File "{}" could not be found. Please, make sure it exists and you have rights to read it.\nProgram will terminate now.'.format(  # pylint: disable=C0301
                self.country_file))
            exit(404)
        return return_dictionary

