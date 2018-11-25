#adds properties to geojson file
import csv
import json
new = 'income.json'
cssvfile = 'Income.csv'
j1 = 'cleaned2000.json'   #2010

f = open(cssvfile, 'r')
reader = csv.reader(f)
stats = {}
next(reader)
heading = next(reader)
for row in reader:
    stats[row[2].split(',')[0].split()[-1]] = {'Income per capita':row[3],}
print(stats)
# print(heading)

j = open(j1)
data = json.load(j)
newdata = {"type":"FeatureCollection",
    "features": []}

for feature in data['features']:
    if feature['properties']['NAME'] in stats:
        feature['properties'].update( stats[feature['properties']['NAME']])
        newdata['features'].append({'type': 'Feature', 'properties':feature['properties'], 'geometry': feature['geometry']})
with open(new, 'w') as outfile:
    json.dump(newdata, outfile)