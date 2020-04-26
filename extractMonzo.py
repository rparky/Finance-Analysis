import pandas as pd
from datetime import datetime

from Utils import count_file_rows
import DataFrame as DF


def extract_monzo():
    records = extract_monzo_file('Monzo/AllTime.csv')
    return records


def extract_monzo_file(filename):
    file = open(filename, encoding="utf8")
    skip = 1
    row_count = count_file_rows(file, skip)
    for i in range(skip):
        next(file, None) 
    temp_store = DF.new_dict(row_count)
    for index, row in enumerate(file):
        extract_entry(index, row, temp_store)
    data = pd.DataFrame.from_dict(temp_store)
    return data


def extract_entry(index, row, temp_store):
    row2 = row.replace('"', '')
    data = row2.split(',')
    date_time = datetime.strptime(data[1], '%Y-%m-%dT%H:%M:%SZ')
    temp_store['Date'][index] = date_time.date()
    temp_store['Time'][index] = date_time.time()
    temp_store['Amount'][index] = float(data[2])
    temp_store['Catagory'][index] = data[6]
    temp_store['Text'][index] = data[8] + ' ' + data[10]
    temp_store['Location'][index] = data[9]
    temp_store['Bank'][index] = 'Monzo'
    temp_store['Account'][index] = 'Standard'
    temp_store['Direction'][index] = float(data[2]) >= 0
    temp_store['Method'][index] = 'card'
    temp_store['Local Currency'][index] = data[5]
    temp_store['Local Amount'][index] = data[4]
    temp_store['Payment Date'][index] = datetime.strptime(data[1], '%Y-%m-%dT%H:%M:%SZ')