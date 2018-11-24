import time
import csv

def collect_data(checker, query):
	if checker == "yes":
		with open('data/test_data.csv', 'r') as csvfile:
			data_reader = csv.reader(csvfile)
			data = list(data_reader)

		data.append(query)
		time.sleep(2)
		return data
	else:
		return ['FAILURE']
