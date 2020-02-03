# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 20:55:15 2019

@author: rpark
"""
import pandas as pd
import DataFrame as DF
from datetime import datetime
from Utils import countFileRows

def extractMonzo():
    records = extractMonzoFile('Monzo/AllTime.csv')
    return records

def extractMonzoFile(filename):
    file = open(filename, encoding="utf8")
    skip = 1
    row_count = countFileRows(file, skip)
    for i in range(skip):
        next(file, None) 
    temp_store = DF.newDict(row_count)
    for index, row in enumerate(file):
        row2=row.replace('"','')
        data=row2.split(',')
        date_time = datetime.strptime(data[1],'%Y-%m-%dT%H:%M:%SZ')
        temp_store['Date'][index] = date_time.date()
        temp_store['Time'][index] = date_time.time()
        temp_store['Amount'][index] = float(data[2])    
        temp_store['Catagory'][index] = data[6]
        temp_store['Text'][index] = data[8] + ' ' + data[10]
        temp_store['Location'][index] = DF.Location(street=data[9])
        temp_store['Bank'][index] = 'Monzo'
        temp_store['Account'][index] = 'Standard'
        temp_store['Direction'][index] = float(data[2])>=0
        temp_store['Method'][index] = 'card'
        temp_store['Local Currency'][index] = data[5]
        temp_store['Local Amount'][index] =data[4]
        temp_store['Payment Date'][index]  = datetime.strptime(data[1],'%Y-%m-%dT%H:%M:%SZ')
    data = pd.DataFrame.from_dict(temp_store)
    return data