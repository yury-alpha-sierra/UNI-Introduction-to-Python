#!C:/Users/yury_/Anaconda3/python.exe
# -*- coding: utf-8 -*-

import csv
import sys

# this is a base directory where all the data/csv files are kept
dataBaseDirectory = './/data//'

def importEconomyLetterPriceDataFromCsvFile(*argv):
    returnedDictionary = {}
    # field_names = 'weight','zone 1','zone 2','zone 3'

    with open(dataBaseDirectory + argv[0], 'r') as inputFile:
        inputFileReader = csv.DictReader(inputFile,fieldnames=argv[1:])
        for arguments in argv[1:]:
            print(arguments)
        for eachLine in inputFileReader:
            returnedDictionary[eachLine[argv[1]]] = eachLine[argv[2]],eachLine[argv[3]],eachLine[argv[4]]

    return returnedDictionary

economyLetterPriceData = {}
economyLetterPriceData = importEconomyLetterPriceDataFromCsvFile('Economy Letters Price Guide ($).csv','weight','zone 1','zone 2','zone 3')

print(economyLetterPriceData.values())
print(economyLetterPriceData.keys())
for d in  economyLetterPriceData.keys():
    print(d)
for d in  economyLetterPriceData.values():
    print(d)
