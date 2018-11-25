#formats geojson file with basic geographic data 
import json

f = open('2000.json', 'r')
data = json.load(f)
newdata = {"type":"FeatureCollection",
    "features": []}
# important = {'GEOID10', 'NAMELSAD10'}
for feature in data['features']:
    if feature['properties']['COUNTY'] == '025':
        dic = feature['properties']
        # print({key:value for key, value in feature['properties'].items() if key in important}) "STATE":"25","COUNTY":"009","TRACT":"267102",
        newdata['features'].append({'type': 'Feature', 'properties':{'NAME':dic["NAME"]}, 'geometry': feature['geometry']})

print(newdata)

with open('cleaned2000.json', 'w') as outfile:
    json.dump(newdata, outfile)