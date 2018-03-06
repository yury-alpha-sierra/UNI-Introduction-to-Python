import csv

with open('.//data//Countries and Zones.csv','r') as contryAndZone:
    contryAndZoneReader = csv.reader(contryAndZone)
    next(contryAndZoneReader)
    for eachLine in contryAndZoneReader:
        print(eachLine[0:2])