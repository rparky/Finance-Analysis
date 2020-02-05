from datetime import datetime
import DataFrame as DF
import pandas as pd
from Utils import countFileRows
import glob


def extract_TSB():
    enhance = extractFolder('ClassicEnhance')
    plus = extractFolder('ClassicPlus')
    easy = extractFolder('EasySaver')
    isa = extractFolder('ISA')
    records = pd.concat([enhance, plus, easy, isa])
    return records


def extractFolder(account):
    extension = 'TSB/' + account
    files = glob.glob(extension + '/*.csv')
    list_of_df = [extractFile(file, account) for file in files]
    records = pd.concat(list_of_df)
    return records

def extractFile(filename, account):
    file = open(filename)
    skip = 1
    row_count = countFileRows(file, skip)
    for i in range(skip):
        next(file, None)
    temp_store = DF.newDict(row_count)
    for index, row in enumerate(file):
        data = row.split(',')
        date_time = datetime.strptime(data[0], '%Y-%m-%d')
        temp_store['Date'][index] = date_time.date()
        temp_store['Time'][index] = date_time.time()
        temp_store['Amount'][index] = extractAmount(data)
        temp_store['Text'][index] = data[4]
        temp_store['Bank'][index] = 'TSB'
        temp_store['Account'][index] = account
        temp_store['Method'][index] = data[1]

    records = pd.DataFrame.from_dict(temp_store)
    return records

def extractAmount(data):
    if len(data[5])!=0:
        amount=-float(data[5])
    else:
        amount=float(data[6])
    return amount;