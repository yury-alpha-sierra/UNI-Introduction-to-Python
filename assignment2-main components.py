import pandas as pd
import re
import csv
from pprint import pprint


class Application:
    def __init__(self, name, dataDir):
        self.name = name
        self.servicesCollection = []
        self.serviceNameCollection = {}
        self.dataBaseDirectory = dataDir
        self.country = ''
        self.weight = 0

    def registerService(self, name, file):
        self.serviceNameCollection[name] = file

    def instantiateService(self):
        for eachService in self.serviceNameCollection:
            self.servicesCollection.append(service(eachService, self.dataBaseDirectory, self.serviceNameCollection.get(eachService)))

    def getAvailableOptions(self):
        for eachService in self.servicesCollection:
             print('{} --> {}'.format(eachService.getServiceName(),eachService.getServicePrice(self.country, self.weight)))


class service:
    def __init__(self, name, dataDir, dataFile):
        self.name = name
        self.dataDir = dataDir
        self.dataFile = dataFile
        self.countryFile = 'Countries and Zones.csv'
        self.zoneWeightData = {}
        self.countryAndZoneData = {}

        self.countryAndZoneData = self.importCountryAndZoneData()
        self.zoneWeightData = self.importDataFromCsvFile()

    def importDataFromCsvFile(self):
        dataInDictionaryFormat = {}
        try:
            dataInDictionaryFormat = pd.read_csv(
                self.dataDir + self.dataFile, header=0, index_col=0, squeeze=True).to_dict()
        except (FileNotFoundError):
            print('File "{}" could not be found. Please, make sure it exists and you have rights to read it.\nProgram will terminate now.'.format(self.dataFile))
            exit(404)
        return dataInDictionaryFormat

    def importCountryAndZoneData(self):
        returnDictionary = {}
        try:
            with open(self.dataDir + self.countryFile) as csvFile:
                # next(csvFile)
                for eachLine in csvFile.readlines():
                    eachLine = eachLine.split(',')
                    returnDictionary[eachLine[0]] = eachLine[1]
        except(FileNotFoundError):
            print('File "{}" could not be found. Please, make sure it exists and you have rights to read it.\nProgram will terminate now.'.format(self.countryFile))
            exit(404)
        return returnDictionary

    def getZoneLabel(self, dictionary, zone):
        zonePattern = re.compile(r'(' + str(zone) + ')')
        zoneLabel = None

        for i in self.zoneWeightData.keys():
            matches = re.search(zonePattern, i)
            if matches is not None:
                zoneLabel = i
        return zoneLabel

    def getWeightLabel(self, dictionary, weight):

        i = None
        for i in dictionary.values():
            keyList = list(i.keys())

        weightNumberPattern = re.compile(r'\d{1,3}')
        weighUnitPattern = re.compile(r'\d{1,3}(kg)')
        j = 0
        while j < len(keyList):
            numberMatches = re.findall(weightNumberPattern, keyList[j])
            unitMatches = re.findall(weighUnitPattern, keyList[j])

            # if found 'kg after the number prepare to convert to gr, otherwise make sure it stays in gr
            if not (len(unitMatches) == 0):
                unitMultiplier = 1000
            else:
                unitMultiplier = 1

            if not (len(numberMatches) == 0):  # if numbers are found in the label
                # if only one number id found like in 'up to 500gr' or 'up to 1 kg'
                if len(numberMatches) == 1:
                    if float(weight) <= float(float(unitMultiplier) * float(numberMatches[0])):
                        return(keyList[j])
                if len(numberMatches) == 2:
                    if (float(weight) >= float(unitMultiplier * float(numberMatches[0]))) and (float(weight) <= float(unitMultiplier * float(numberMatches[1]))):
                        return(keyList[j])
            j += 1
        return None

    def getServicePrice(self, country, weight):
        zone = self.getZoneInfoFromCountry(self.countryAndZoneData, country)
        try:
           return float(self.zoneWeightData.get(self.getZoneLabel(self.zoneWeightData, zone)).get(str(self.getWeightLabel(self.zoneWeightData, weight))))
        except(ValueError, AttributeError, TypeError):
            return None
        return

    def isServicableCountry(self, dictionary, countryName):
        if countryName in dictionary:
            return True
        else:
            return False

    def getZoneInfoFromCountry(self, dictionary, countryName):
        if self.isServicableCountry(dictionary, countryName):
            result = dictionary.get(countryName)
            numberPattern = re.compile(r'\d{1}')
            matches = re.findall(numberPattern, result)
            if not (len(matches) == 0):
                return matches[0]
        else:
            return None

    def getServiceName(self):
        return self.name


postageService = Application('Postage Service', './/data//')
postageService.country = 'New Zealand'
postageService.weight = 150

postageService.registerService('Economy Letter','Economy Letters Price Guide ($).csv')
postageService.registerService('Economy Parcel by Air','Economy Parcel Price Guide_by Air ($).csv')
postageService.registerService('Economy Parcel by Sea', 'Economy Parcel Price Guide_by Sea ($).csv')
postageService.registerService('Express Letter', 'Express Letter Price Guide ($).csv')
postageService.registerService('Express Parcel', 'Express Parcel Price Guide ($).csv')
postageService.registerService('Standard Parcel','Standard Parcel Price Guide ($).csv')

postageService.instantiateService()

pprint(postageService.serviceNameCollection)
pprint(postageService.servicesCollection)

postageService.getAvailableOptions()
