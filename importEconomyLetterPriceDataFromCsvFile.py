#!C:/Users/yury_/Anaconda3/python.exe
# -*- coding: utf-8 -*-

import csv
import sys

# this is a base directory where all the data/csv files are kept
dataBaseDirectory = './/data//'

def importEconomyLetterPriceDataFromCsvFile(filename,*argv):
    returnedDictionary = {}

    with open(dataBaseDirectory + filename, 'r') as inputFile:
        inputFileReader = csv.DictReader(inputFile,fieldnames=None)

        for eachLine in inputFileReader:
            returnedDictionary.update(eachLine)

    return returnedDictionary

economyLetterPriceData = {}
economyLetterPriceData = importEconomyLetterPriceDataFromCsvFile('Economy Letters Price Guide ($).csv' ,'Col1','Col2','Col3','Col4')

print(economyLetterPriceData.values())
print(economyLetterPriceData.keys())
for d in  economyLetterPriceData.keys():
    print(d)
for d in  economyLetterPriceData.values():
    print(d)
