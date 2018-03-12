import pandas as pd
import re as re
dataBaseDirectory = './/data//'

def importPriceDataFromCsvFile(filename):
    returnedDictionary = {}

    returnedDictionary = pd.read_csv(dataBaseDirectory + filename, header=0, index_col=0, squeeze=True).to_dict()

    return returnedDictionary

def getZoneLabel(zone):
    zonePattern = re.compile('['+ str(zone) + ']')
    y = None
    for i in economyLetterPriceData.keys():
        match = re.search(zonePattern,i)
        if match is not None:
            y = i
    return y

economyLetterPriceData = {}
economyLetterPriceData = importPriceDataFromCsvFile('Economy Letters Price Guide ($).csv')

zone = 6

print(economyLetterPriceData.get(getZoneLabel(zone)).get('Up to 50g'))