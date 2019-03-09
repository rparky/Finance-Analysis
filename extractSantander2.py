# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 21:23:28 2018

@author: rpark
"""

from datetime import datetime
import DataFrame as DF
import pandas as pd
from Utils import countFileRows

def extractSantander():
    files = ['2013', '2014', '2015', '2016', '2017', '2018']  
    current = extractFolder('Current', 'Santander/Current/', files, '.txt')
    files = ['2017', '2018']
    savings = extractFolder('Savings', 'Santander/Savings/', files, '.txt')
    records = pd.concat([current, savings])
    return records;

def extractFolder(account, extension, files, filetype):
    records = DF.newDataFrame(0)
    for file in files:
        records = pd.concat([records, extractFile(extension + 
                                                  file + filetype, account)])
    return records
    
def extractFile(filename,account):
    file = open(filename)
    skip = 4
    row_count = countFileRows(file, skip)
    for i in range(skip):
        next(file, None) 
    temp_store = DF.newDict(row_count)
    for index, row in enumerate(file):   
        temp_index = int(index / 5)
        temp_row = index % 5              
        if temp_row == 0:
            temp = row.split('\xa0')
            temp = temp[1].split('\n')
            temp_store['Date'][temp_index] = datetime.strptime(temp[0],'%d/%m/%Y')
        elif temp_row == 1:
            temp_store['Text'][temp_index] = row[13:]
        elif temp_row == 2:
            temp = row.split('\xa0') [1].split('\n')
            temp_store['Amount'][temp_index] = float(temp[0])
        temp_store['Bank'][temp_index] = 'Santander'
        temp_store['Account'][temp_index] = account
    
    records = pd.DataFrame.from_dict(temp_store)
    return records;