# this is a base directory where all the data/csv files are kept
import csv 
dataBaseDirectory = './/data//'

def importEconomyLetterPriceDataFromCsvFile(filename,*argv):
    returnedDictionary = {}
    # field_names = 'weight','zone 1','zone 2','zone 3'

    with open(dataBaseDirectory + filename, 'r') as inputFile:
        inputFileReader = csv.DictReader(inputFile,fieldnames=None)
        # for arguments in argv[1:]:
        #     print(arguments)
        for eachLine in inputFileReader:
            k = eachLine.items()
            # returnedDictionary[k] = eachLine[1:]

    return returnedDictionary
# import csv
# reader = csv.reader(open('filename.csv', 'r'))
# d = {}
# for row in reader:
#    k, v = row
#    d[k] = v
economyLetterPriceData = {}
economyLetterPriceData = importEconomyLetterPriceDataFromCsvFile('Economy Letters Price Guide ($).csv' ,'Col1','Col2','Col3','Col4')

print(economyLetterPriceData.values())
# print(economyLetterPriceData.keys())
# for d in  economyLetterPriceData.keys():
#     print(d)
# for d in  economyLetterPriceData.values():
#     print(d)
