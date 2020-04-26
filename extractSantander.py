from datetime import datetime
import pandas as pd
import glob
import numpy as np

import DataFrame as DF
from Utils import count_file_rows


def extract_santander():
    current = extract_folder('Current')
    records = current
    return records;


def extract_folder(account):
    extension = 'Santander/' + account
    files = glob.glob(extension + '/*.txt')
    list_of_df = [extract_file(file, account) for file in files]
    records = pd.concat(list_of_df)
    return records


def extract_file(filename, account):
    file = open(filename)
    skip = 4
    rows_per_entry = 5
    row_count = int(np.ceil(count_file_rows(file, skip) / rows_per_entry))
    for i in range(skip):
        next(file, None) 
    temp_store = DF.new_dict(row_count)
    for index, row in enumerate(file):
        extract_entry(index, row, temp_store, rows_per_entry, account)
    records = pd.DataFrame.from_dict(temp_store)
    return records


def extract_entry(index, row, temp_store, rows_per_entry, account):
    temp_index = int(index / rows_per_entry)
    temp_row = index % rows_per_entry

    temp_store['Bank'][temp_index] = 'Santander'
    temp_store['Account'][temp_index] = account


def manage_row(temp_row, row, temp_store, temp_index):
    if temp_row == 0:
        temp = row.split('\xa0')
        temp = temp[1].split('\n')
        date_time = datetime.strptime(temp[0], '%d/%m/%Y')
        temp_store['Date'][temp_index] = date_time.date()
        temp_store['Time'][temp_index] = date_time.time()
    elif temp_row == 1:
        temp_store['Text'][temp_index] = row[13:]
    elif temp_row == 2:
        temp = row.split('\xa0')[1].split('\n')
        temp_store['Amount'][temp_index] = float(temp[0])
