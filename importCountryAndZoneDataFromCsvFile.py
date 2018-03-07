import csv

# this is a base directory where all the data/csv files are kept
dataBaseDirectory = './/data//'

def importDataFromFile(fileName,keyCol,*argv):
    returnedDictionary = {}

    with open(dataBaseDirectory + fileName, 'r') as inputFile:
        inputFileReader = csv.DictReader(inputFile)

        for eachLine in inputFileReader:
            returnedDictionary[eachLine[keyCol]] = eachLine[argv[0]]

    return returnedDictionary


countryAndZoneData = {}
countryAndZoneData = importDataFromFile('Countries and Zones.csv','Destination country','Zones')
print(len(countryAndZoneData))
print(countryAndZoneData)

country = 'Iran - Islamic Republic Of'
print(countryAndZoneData.get(country))