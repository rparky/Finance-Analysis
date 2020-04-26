from datetime import datetime
import glob
import pandas as pd

from Utils import count_file_rows
import DataFrame as DF


def extract_nationwide():
    flexsclusive = extract_folder('FlexclusiveSaver')
    flexidirect = extract_folder('FlexiDirect')
    isa = extract_folder('ISA')
    records = pd.concat([flexsclusive, flexidirect, isa])
    return records


def extract_folder(account):
    extension = 'Nationwide/' + account
    files = glob.glob(extension + '/*.csv')
    list_of_df = [extract_file(file, account) for file in files]
    records = pd.concat(list_of_df)
    return records


def extract_file(filename, account):
    file = open(filename)
    skip = 5
    row_count = count_file_rows(file, skip)
    for i in range(skip):
        next(file, None)
    temp_store = DF.new_dict(row_count)
    for index, row in enumerate(file):
        extract_entry(index, row, temp_store, account)
    records = pd.DataFrame.from_dict(temp_store)
    return records


def extract_entry(index, row, temp_store, account):
    row2 = row.replace('"', '')
    data = row2.split(',')
    date_time = datetime.strptime(data[0], '%d %b %Y')
    temp_store['Date'][index] = date_time.date()
    temp_store['Time'][index] = date_time.time()
    temp_store['Amount'][index] = get_amount(data[4], data[3])
    temp_store['Text'][index] = data[2]
    temp_store['Bank'][index] = 'Nationwide'
    temp_store['Account'][index] = account
    temp_store['Method'][index] = data[1]


def get_amount(in_, out_):
    val=0
    if len(in_) != 0:
        val += float(in_[1:])
    if len(out_) != 0:
        val -= float(out_[1:])
    return val
