import csv

# this is a base directory where all the data/csv files are kept
dataBaseDirectory = './/data//'

def importEconomyLetterPriceDataFromCsvFile(fileName,keyCol,*argv):
    returnedDictionary = {}

    with open(dataBaseDirectory + fileName, 'r') as inputFile:
        inputFileReader = csv.DictReader(inputFile)

        for eachLine in inputFileReader:
            returnedDictionary[eachLine[keyCol]] = eachLine[argv[0]],eachLine[argv[1]],eachLine[argv[2]]

    return returnedDictionary

economyLetterPriceData = {}
economyLetterPriceData = importEconomyLetterPriceDataFromCsvFile('Economy Letters Price Guide ($).csv','Weight','Zone 1','Zone 2,3 and 5','Zone 4, 6, 7 and 9')

print(economyLetterPriceData)
