import csv
f = open('Testing racial data.csv', 'r')
reader = csv.reader(f)
newrows = []
for row in reader:
    newrow = row
    newrow[1] = row[1][0:3]+row[1][8:16]
    newrows.append(newrow)

    # print(newrow)
    # print(row[1], row[1][0:3]+row[1][8:16])

print(newrows)
with open('test.csv', 'w', newline = '') as f:
    writer = csv.writer(f)
    writer.writerows(newrows)



