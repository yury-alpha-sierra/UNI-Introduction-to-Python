import pandas as pd
import re
import csv


class Application:
    def __init__(self, name, dataDir):
        self.name = name
        self.servicesCollection = {}
        self.dataBaseDirectory = dataDir
        self.country = ''
        self.weight = 0

    def registerService(self, name, object):
        pass


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
            print('File {} could not be found. Please, make sure it exists and you have rights to read it.\nProgram will terminate now.'.format(self.dataFile))
            exit(404)
        return dataInDictionaryFormat

    def importCountryAndZoneData(self):
        returnDictionary = {}
        with open(self.dataDir + self.countryFile) as csvFile:
            # next(csvFile)
            for eachLine in csvFile.readlines():
                eachLine = eachLine.split(',')
                returnDictionary[eachLine[0]] = eachLine[1]
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


postageService = Application('Postage Service', './/data//')
postageService.country = 'New Zealand'
postageService.weight = 150

economyLetterService = service(
    'Economy Letter', postageService.dataBaseDirectory, 'Economy Letters Price Guide ($).csv')
economyParcelByAirService = service(
    'Economy Parcel by Air', postageService.dataBaseDirectory, 'Economy Parcel Price Guide_by Air ($).csv')
economyParcelBySeaService = service(
    'Economy Parcel by Sea', postageService.dataBaseDirectory, 'Economy Parcel Price Guide_by Sea ($).csv')
expressLetterService = service(
    'Express Letter', postageService.dataBaseDirectory, 'Express Letter Price Guide ($).csv')
expressParcelService = service(
    'Express Parcel', postageService.dataBaseDirectory, 'Express Parcel Price Guide ($).csv')
standardPrcelService = service(
    'Standard Parcel', postageService.dataBaseDirectory, 'Standard Parcel Price Guide ($).csv')


print('Economy Letter --> {}'.format(economyLetterService.getServicePrice(
    postageService.country, postageService.weight)))
print('Economy Parcel by Air --> {}'.format(economyParcelByAirService.getServicePrice(
    postageService.country, postageService.weight)))
print('Economy Parcel by Sea --> {}'.format(economyParcelBySeaService.getServicePrice(
    postageService.country, postageService.weight)))
print('Express Letter --> {}'.format(expressLetterService.getServicePrice(
    postageService.country, postageService.weight)))
print('Express Parcel --> {}'.format(expressParcelService.getServicePrice(
    postageService.country, postageService.weight)))
print('Standard Parcel--> {}'.format(standardPrcelService.getServicePrice(
    postageService.country, postageService.weight)))
