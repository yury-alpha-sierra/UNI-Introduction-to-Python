import pandas as pd
import re as re


dataBaseDirectory = './/data//'


def importPriceDataFromCsvFile(filename):

    priceDataInDictionaryFormat = {}

    priceDataInDictionaryFormat = pd.read_csv(
        dataBaseDirectory + filename, header=0, index_col=0, squeeze=True).to_dict()

    return priceDataInDictionaryFormat


def getZoneLabel(dictionary, zone):

    zonePattern = re.compile(r'[' + str(zone) + ']')
    y = None

    for i in dictionary.keys():

        if re.search(zonePattern, i) is not None:
            y = i

    return y


def getWeightLabel(dictionary, weight):
    i = None
    for i in dictionary.values():
        keyList = list(i.keys())

    weightPattern = re.compile(r'\d{2,3}')
    j = 0
    while j < len(keyList):
        matches = re.findall(weightPattern, keyList[j])

        if len(matches) == 1:
            if weight <= int(matches[0]):
                return(keyList[j])
        else:
            if (weight >= int(matches[0])) and (weight <= int(matches[1])):
                return(keyList[j])
        j += 1


zone = 6
weight = 360

economyLetterPriceData = {}
economyLetterPriceData = importPriceDataFromCsvFile(
    'Economy Letters Price Guide ($).csv')
print(economyLetterPriceData.get(getZoneLabel(economyLetterPriceData,zone)).get(str(getWeightLabel(economyLetterPriceData,weight))))


economyParcelByAirPriceData = {}
economyParcelByAirPriceData = importPriceDataFromCsvFile(
    'Economy Parcel Price Guide_by Air ($).csv')
print(economyParcelByAirPriceData.get(getZoneLabel(economyParcelByAirPriceData,zone)).get(str(getWeightLabel(economyParcelByAirPriceData,weight))))


economyParcelBySeaPriceData = {}
economyParcelBySeaPriceData = importPriceDataFromCsvFile(
    'Economy Parcel Price Guide_by Air ($).csv')
print(economyParcelBySeaPriceData.get(getZoneLabel(economyParcelBySeaPriceData,zone)).get(str(getWeightLabel(economyParcelBySeaPriceData,weight))))