import csv
import json

f = open('Boston_spending_percent.csv', 'r')
reader = csv.reader(f)
next(reader)
newdat = {'labels': [], 'datasets': []}
for row in reader:
    print(row)
    newdat['labels'].append(row[0])
    newdat['datasets'].append({'label':"percent", 
    'data': [row[1], row[2]]})
with open('spending.json', 'w') as outfile:
    json.dump(newdat, outfile)
# var chartData = {
#    labels: Object.keys(items.dates),
#    datasets: [{
#       label: "Reps",
#       backgroundColor: "blue",
#       data: [7, 8, 3]
#    }, {
#       label: "Reps",
#       backgroundColor: "red",
#       data: [0, 9, 7]
#    }, {
#       label: "Reps",
#       backgroundColor: "green",
#       data: [0, 10, 12]
#    }]
# };