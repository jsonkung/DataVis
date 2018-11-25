import pandas as pd
import os
import statistics as stat
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

def open_file(filename,header='infer'):
    try:
        path = 'datavis/data/{}'.format(filename)
        return pd.read_csv(path,header=header)
    except FileNotFoundError:
        raise NameError('file `{}` not found in data folder'.format(filename))


def get_single_bar_data(filename,method=stat.mean,header='infer'):
    '''
    Assuming csv has two columns and column 1 is x and column 2 is y
    returns labels and aggregate values based on method

    Params:
        filename - string with name of csv file
        method - method of aggregating data (e.g. mean, mode)
        header - status of headers in csv to determine axes

    Returns:
        dictionary with attributes
            axis - list of axes names
            labels - list of labels for data
            data - list of aggregated data in same order as labels
    '''
    # Generate pandas df from csv
    data = open_file(filename,header)
    out = {}
    # Reserved attribute names in output
    reserved = ['axes','labels','data']

    # Generate axes names if exists
    if header is not None:
        out['axes'] = list(data)
    else:
        out['axes'] = None
    # Aggregate data of same input
    for idx,x,y in data.itertuples():
        if x not in out:
            out[x] = []
        out[x].append(float(y.replace(',','')))

    out['labels'] = []
    out['data'] = []
    attributes = list(out.keys())

    # Perform method on aggregate data in output
    for attr in attributes:
        if attr not in reserved:
            out['labels'].append(attr)
            out['data'].append(method(out[attr]))
            del out[attr]

    return out
