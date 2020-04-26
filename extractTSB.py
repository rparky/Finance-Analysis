from datetime import datetime
import glob
import pandas as pd

from Utils import count_file_rows
import DataFrame as DF


def extract_TSB():
    enhance = extract_folder('ClassicEnhance')
    plus = extract_folder('ClassicPlus')
    easy = extract_folder('EasySaver')
    isa = extract_folder('ISA')
    records = pd.concat([enhance, plus, easy, isa])
    return records


def extract_folder(account):
    extension = 'TSB/' + account
    files = glob.glob(extension + '/*.csv')
    list_of_df = [extract_file(file, account) for file in files]
    records = pd.concat(list_of_df)
    return records


def extract_file(filename, account):
    file = open(filename)
    skip = 1
    row_count = count_file_rows(file, skip)
    for i in range(skip):
        next(file, None)
    temp_store = DF.new_dict(row_count)
    for index, row in enumerate(file):
        extract_entry(index, row, temp_store, account)
    records = pd.DataFrame.from_dict(temp_store)
    return records


def extract_entry(index, row, temp_store, account):
    data = row.split(',')
    date_time = datetime.strptime(data[0], '%Y-%m-%d')
    temp_store['Date'][index] = date_time.date()
    temp_store['Time'][index] = date_time.time()
    temp_store['Amount'][index] = extract_amount(data)
    temp_store['Text'][index] = data[4]
    temp_store['Bank'][index] = 'TSB'
    temp_store['Account'][index] = account
    temp_store['Method'][index] = data[1]


def extract_amount(data):
    if len(data[5]) != 0:
        amount = -float(data[5])
    else:
        amount = float(data[6])
    return amount
