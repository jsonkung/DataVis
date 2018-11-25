import csv
import json

race = open('RacialData2.csv', 'r')
reader = csv.reader(race)
racestats = {}
next(reader)
heading = next(reader)
for row in reader:
    # print(len(row))
    racestats[row[1]] = {'Total Population': row[3], 'Percent Hispanic': row[12], 'Percent White': row[13], 'Percent Black': row[14], 'Percent Asian': row[15]}

genderage = open('genderage.csv', 'r')
reader = csv.reader(genderage)
gastats = {}
next(reader)
heading = next(reader)
for row in reader:
    gastats[row[1]] = {"% seniors": row[-2], '% Children':row[-1]}

final = []
for key in gastats:
    if key in racestats:
        racestats[key].update(gastats[key])
        final.append(racestats[key])

with open('datavis1.json', 'w') as outfile:
    json.dump(final, outfile)



