import pandas as pd
import re as re


dataBaseDirectory = './/data//'


def importPriceDataFromCsvFile(filename):

    priceDataInDictionaryFormat = {}

    priceDataInDictionaryFormat = pd.read_csv(
        dataBaseDirectory + filename, header=0, index_col=0, squeeze=True).to_dict()

    return priceDataInDictionaryFormat


def getZoneLabel(zone):

    zonePattern = re.compile(r'[' + str(zone) + ']')
    y = None

    for i in economyLetterPriceData.keys():

        if re.search(zonePattern, i) is not None:
            y = i

    return y


economyLetterPriceData = {}
economyLetterPriceData = importPriceDataFromCsvFile(
    'Economy Letters Price Guide ($).csv')


def getWeightLabel(dictionary, weight):
    i = None
    for i in dictionary.values():
        keyList = list(i.keys())

    weightPattern = re.compile(r'\d{2,3}')
    j = 0

    while j < len(keyList):
        matches = re.findall(weightPattern, keyList[j])

        # print('keylist {}  j={}  matches = {}'.format(keyList[j], j, matches))

        if len(matches) == 1:
            if weight <= int(matches[0]):
                return(keyList[j]) 
        else:
            if (weight >= int(matches[0])) and (weight <= int(matches[1])):
                return(keyList[j]) 
        j += 1
        

print(getWeightLabel(economyLetterPriceData,830))