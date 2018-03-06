import csv

# this is a base directory where all the data/csv files are kept
dataBaseDirectory = './/data//'

with open(dataBaseDirectory + 'Countries and Zones.csv','r') as contryAndZone:
    contryAndZoneReader = csv.reader(contryAndZone)

    next(contryAndZoneReader)   # get rid of the csv file first row that had column headers in it

    for eachLine in contryAndZoneReader:
        print(eachLine[0:2])   # make sure we are reading first two columns. Import using csv reader imports many more columns for some reason????