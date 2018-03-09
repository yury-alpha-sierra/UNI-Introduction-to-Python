import csv

# this is a base directory where all the data/csv files are kept
dataBaseDirectory = './/data//'


def importDataFromFile(fileName,column1,column2,column3,column4):
    returnedDictionary = {column1:'',column2:'',column3:'',column4:'',}

    with open(dataBaseDirectory + fileName, 'r') as inputFile:
        inputFileReader = csv.DictReader(inputFile)

        for eachLine in inputFileReader:
                returnedDictionary[eachLine[column1]] = eachLine[column2]
    return returnedDictionary

# countryAndZoneData = {}
# countryAndZoneData = importDataFromFile('Countries and Zones.csv','Destination country','Zones')
# print(len(countryAndZoneData))
# print(countryAndZoneData)

data = {}
data = importDataFromFile('Economy Letters Price Guide ($).csv','Weight sdcdws','Zone 1','Zone 2,3 and 5','Zone 4, 6, 7 and 9')
print(len(data))
print(data)

