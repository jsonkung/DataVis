# adds correct geoid values to csv 
import csv
import json
unparsed = 'commute time.csv'
new = 'commute.csv'

# f = open('MA Census.csv', 'r')
# reader = csv.reader(f)
# tractnum = {}
# for row in reader:
#     tractnum[row[3].split(',')[0]] = row[2][7:]
# 1580000US2507000025000100
f = open(unparsed, 'r')
reader = csv.reader(f)
next(reader)
header = next(reader)
newrows = [header]
for row in reader:
    print(str(row[0][9:11])+str(row[0][16:]))
#     newrow = row
#     newrow[1] = row[0][9:12]+row[0][16:]
#     tract = row[2].split(',')[0]
#     newrow[1] = tractnum.get(tract, 'ERROR')
#     newrows.append(newrow)

# with open(new, 'w', newline = '') as f:
#     writer = csv.writer(f)
#     writer.writerows(newrows)
    