from datetime import datetime
import DataFrame as DF
import pandas as pd
from Utils import countFileRows
import glob


def extract_nationwide():
    flexsclusive = extractFolder('FlexclusiveSaver')
    flexidirect = extractFolder('FlexiDirect')
    isa = extractFolder('ISA')
    records = pd.concat([flexsclusive, flexidirect, isa])
    return records


def extractFolder(account):
    extension = 'Nationwide/' + account
    files = glob.glob(extension + '/*.csv')
    list_of_df = [extractFile(file, account) for file in files]
    records = pd.concat(list_of_df)
    return records

def extractFile(filename, account):
    file = open(filename)
    skip = 5
    row_count = countFileRows(file, skip)
    for i in range(skip):
        next(file, None)
    temp_store = DF.newDict(row_count)
    for index, row in enumerate(file):
        row2 = row.replace('"', '')
        data = row2.split(',')
        date_time = datetime.strptime(data[0], '%d %b %Y')
        temp_store['Date'][index] = date_time.date()
        temp_store['Time'][index] = date_time.time()
        temp_store['Amount'][index] = getAmount(data[4], data[3])
        temp_store['Text'][index] = data[2]
        temp_store['Bank'][index] = 'Nationwide'
        temp_store['Account'][index] = account
        temp_store['Method'][index] = data[1]

    records = pd.DataFrame.from_dict(temp_store)
    return records

def getAmount(in_, out_):
    val=0
    if len(in_)!=0:
        val+=float(in_[1:])
    if len(out_)!=0:
        val-=float(out_[1:])
    return val