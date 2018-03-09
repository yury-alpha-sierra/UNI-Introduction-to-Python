import csv

# this is a base directory where all the data/csv files are kept
dataBaseDirectory = './/data//'

def importEconomyLetterPriceDataFromCsvFile(fileName):
    returnedDictionary = {}

    with open(dataBaseDirectory + fileName, 'r') as inputFile:
        inputFileReader = csv.DictReader(inputFile)

        for eachLine in inputFileReader:
            returnedDictionary[inputFileReader.fieldnames[0]] = eachLine[inputFileReader.fieldnames[1]],eachLine[inputFileReader.fieldnames[2]],eachLine[inputFileReader.fieldnames[3]]

    return returnedDictionary

economyLetterPriceData = {}
economyLetterPriceData = importEconomyLetterPriceDataFromCsvFile('Economy Letters Price Guide ($).csv')

print(economyLetterPriceData)
