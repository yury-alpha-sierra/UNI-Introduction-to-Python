#!C:/Users/yury_/Anaconda3/python.exe
# -*- coding: utf-8 -*-

import csv
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# this is a base directory where all the data/csv files are kept
dataBaseDirectory = './/data//'

def importEconomyLetterPriceDataFromCsvFile(fileName):
    returnedDictionary = {}
    field_names = 'weight','zone 1','zone 2','zone 3'

    with open(dataBaseDirectory + fileName, 'r') as inputFile:
        inputFileReader = csv.DictReader(inputFile,fieldnames=field_names)

        for eachLine in inputFileReader:
            returnedDictionary[eachLine[inputFileReader.fieldnames[0]]] = eachLine[inputFileReader.fieldnames[1]],eachLine[inputFileReader.fieldnames[2]],eachLine[inputFileReader.fieldnames[3]]

    return returnedDictionary

economyLetterPriceData = {}
economyLetterPriceData = importEconomyLetterPriceDataFromCsvFile('Economy Letters Price Guide ($).csv')


economyLetterPriceDataTableKeys = []
for eachKey in economyLetterPriceData.keys():
    economyLetterPriceDataTableKeys.append(eachKey)
    # print(eachKey)
print(economyLetterPriceDataTableKeys)
# for eachValue in economyLetterPriceData.values():
#     print(eachValue)
