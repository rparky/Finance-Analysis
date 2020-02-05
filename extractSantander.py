from datetime import datetime
import DataFrame as DF
import pandas as pd
from Utils import countFileRows
import glob


def extractSantander():
    current = extractFolder('Current')
    records = current
    return records;


def extractFolder(account):
    extension = 'Santander/' + account
    files = glob.glob(extension + '/*.txt')
    list_of_df = [extractFile(file, account) for file in files]
    records = pd.concat(list_of_df)
    return records

def extractFile(filename, account):
    file = open(filename)
    skip = 4
    row_count = int(countFileRows(file, skip)/5) + 1
    for i in range(skip):
        next(file, None) 
    temp_store = DF.newDict(row_count)
    for index, row in enumerate(file):   
        temp_index = int(index / 5)
        temp_row = index % 5              
        if temp_row == 0:
            temp = row.split('\xa0')
            temp = temp[1].split('\n')
            date_time = datetime.strptime(temp[0],'%d/%m/%Y')
            temp_store['Date'][temp_index] = date_time.date()
            temp_store['Time'][temp_index] = date_time.time()
        elif temp_row == 1:
            temp_store['Text'][temp_index] = row[13:]
        elif temp_row == 2:
            temp = row.split('\xa0')[1].split('\n')
            temp_store['Amount'][temp_index] = float(temp[0])
        temp_store['Bank'][temp_index] = 'Santander'
        temp_store['Account'][temp_index] = account
    
    records = pd.DataFrame.from_dict(temp_store)
    return records
