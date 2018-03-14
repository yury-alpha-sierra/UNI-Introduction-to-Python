import pandas as pd
import re
import csv

# this is a base directory where all the data/csv files are kept
dataBaseDirectory = './/data//'

class Application:
    
   def __init__(self, name, dataDir):
       pass


def importDataFromCsvFile(filename):

    dataInDictionaryFormat = {}
    try:
      dataInDictionaryFormat = pd.read_csv(
           dataBaseDirectory + filename, header=0, index_col=0, squeeze=True).to_dict()
    except (FileNotFoundError):
        print('File {} could not be found. Please, make sure it exists and you have rights to read it.\nProgram will terminate now.'.format(filename))
        exit(404)
    return dataInDictionaryFormat


def getZoneLabel(dictionary, zone):

    zonePattern = re.compile(r'(' + str(zone) + ')')
    zoneLabel = None

    for i in dictionary.keys():
        matches = re.search(zonePattern, i)
        if matches is not None:
            zoneLabel = i

    return zoneLabel


def getWeightLabel(dictionary, weight):
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


def getServicePrice(dictionary, country, weight):
    zone = getZoneInfoFromCountry(countryAndZoneData, country)
    try:
        return float(dictionary.get(getZoneLabel(dictionary, zone)).get(str(getWeightLabel(dictionary, weight))))
    except (ValueError, AttributeError, TypeError):
        return None
    return


def importCountryAndZoneData(filename):
    returnDictionary = {}
    with open(dataBaseDirectory + filename) as csvFile:
        next(csvFile)
        for eachLine in csvFile.readlines():
            eachLine = eachLine.split(',')
            returnDictionary[eachLine[0]] = eachLine[1]
    return returnDictionary


def isServicableCountry(dictionary, countryName):
    if countryName in dictionary:
        return True
    else:
        return False


def getZoneInfoFromCountry(dictionary, countryName):
    if isServicableCountry(dictionary, countryName):
        result = dictionary.get(countryName)
        numberPattern = re.compile(r'\d{1}')
        matches = re.findall(numberPattern, result)
        if not (len(matches) == 0):
            return matches[0]
    else:
        return None

countryAndZoneData = importCountryAndZoneData('Countries and Zones.csv')
economyLetterPriceData = importDataFromCsvFile('Economy Letters Price Guide ($).csv')
economyParcelByAirPriceData = importDataFromCsvFile('Economy Parcel Price Guide_by Air ($).csv')
economyParcelBySeaPriceData = importDataFromCsvFile('Economy Parcel Price Guide_by Sea ($).csv')
expressLetterPriceData = importDataFromCsvFile('Express Letter Price Guide ($).csv')
expressParcelPriceData = importDataFromCsvFile('Express Parcel Price Guide ($).csv')
satandardPrcelPriceData = importDataFromCsvFile('Standard Parcel Price Guide ($).csv')

app = Application('Postage Service','.//data')
country = 'Argentina'
weight = 5000

print('Economy Letter --> {}'.format(getServicePrice(economyLetterPriceData, country, weight)))
print('Economy Parcel by Air --> {}'.format(getServicePrice(economyParcelByAirPriceData, country, weight)))
print('Economy Parcel by Sea --> {}'.format(getServicePrice(economyParcelBySeaPriceData, country, weight)))
print('Express Letter --> {}'.format(getServicePrice(expressLetterPriceData, country, weight)))
print('Express Parcel --> {}'.format(getServicePrice(expressParcelPriceData, country, weight)))
print('Standard Parcel--> {}'.format(getServicePrice(satandardPrcelPriceData, country, weight)))
