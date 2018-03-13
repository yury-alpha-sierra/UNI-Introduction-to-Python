import pandas as pd
import re as re


dataBaseDirectory = './/data//'


def importPriceDataFromCsvFile(filename):

    priceDataInDictionaryFormat = {}

    priceDataInDictionaryFormat = pd.read_csv(
        dataBaseDirectory + filename, header=0, index_col=0, squeeze=True).to_dict()

    return priceDataInDictionaryFormat


def getZoneLabel(dictionary, zone):

    zonePattern = re.compile(r'(' + str(zone) + ')')
    zoneLabel = None

    for i in dictionary.keys():
        matches = re.search(zonePattern, i)
        if matches  is not None:
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

        if not (len(unitMatches) == 0): #if found kg after the number prepare to convert to gr, otherwise make sure it stays in gr
            unitMultiplier = 1000
        else:
            unitMultiplier = 1

        if not (len(numberMatches) == 0): #if numbers are found in the label
            if len(numberMatches) == 1: #if only one number id found like in 'up to 500gr' or 'up to 1 kg'
                if float(weight) <= float(float(unitMultiplier) * float(numberMatches[0])):
                    return(keyList[j])
            if len(numberMatches) == 2:
                if (float(weight) >= float(unitMultiplier * float(numberMatches[0]))) and (float(weight) <= float(unitMultiplier * float(numberMatches[1]))):
                    return(keyList[j])
        j += 1
    return None


def getServicePrice(priceData, zone, weight):
    try:
       return  float(priceData.get(getZoneLabel(priceData, zone)).get(str(getWeightLabel(priceData, weight))))
    except (ValueError, AttributeError):
        return None
    return


zone = 1
weight = 50

economyLetterPriceData = {}
economyLetterPriceData = importPriceDataFromCsvFile(
    'Economy Letters Price Guide ($).csv')
print(getServicePrice(economyLetterPriceData, zone, weight))


economyParcelByAirPriceData = {}
economyParcelByAirPriceData = importPriceDataFromCsvFile(
    'Economy Parcel Price Guide_by Air ($).csv')
print(getServicePrice(economyParcelByAirPriceData, zone, weight))


economyParcelBySeaPriceData = {}
economyParcelBySeaPriceData = importPriceDataFromCsvFile(
    'Economy Parcel Price Guide_by Sea ($).csv')
print(getServicePrice(economyParcelBySeaPriceData, zone, weight))


expressLetterPriceData = {}
expressLetterPriceData = importPriceDataFromCsvFile(
    'Express Letter Price Guide ($).csv')
print(getServicePrice(expressLetterPriceData, zone, weight))


satandardPrcelPriceData = {}
satandardPrcelPriceData = importPriceDataFromCsvFile(
    'Standard Parcel Price Guide ($).csv')
print(getServicePrice(satandardPrcelPriceData, zone, weight))
