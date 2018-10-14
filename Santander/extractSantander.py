# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 21:23:28 2018

@author: rpark
"""

from datetime import datetime
from record  import record


def extractSantander():
     records=extractSantanderCurrent()
     records.extend(extractSantanderSavings())
     return records;

def extractSantanderCurrent():
    records=extractSantanderFile('Santander/Current/SantanderCurrent2012.txt')
    records.extend(extractSantanderFile('Santander/Current/SantanderCurrent2013.txt'))
    records.extend(extractSantanderFile('Santander/Current/SantanderCurrent2014.txt'))
    records.extend(extractSantanderFile('Santander/Current/SantanderCurrent2015.txt'))
    records.extend(extractSantanderFile('Santander/Current/SantanderCurrent2016.txt'))
    records.extend(extractSantanderFile('Santander/Current/SantanderCurrent2017.txt'))
    records.extend(extractSantanderFile('Santander/Current/SantanderCurrent2018.txt'))
    return records;

def extractSantanderSavings():
    records=extractSantanderFile('Santander/Savings/SantanderSavings2017.txt')
    records.extend(extractSantanderFile('Santander/Savings/SantanderSavings2018.txt'))
    return records;

def extractSantanderFile(filename):
    file = open(filename)
    next(file, None) 
    next(file, None) 
    next(file, None) 
    next(file, None) 
    records = []
    temp_rows = [];
    for row in file:  
        
        if(len(temp_rows)!=4):              
            temp_rows.append(row)
        else:
            records.append(extractASantanderRecord(temp_rows))
            temp_rows= []
    
    records.append(extractASantanderRecord(temp_rows))
    records.reverse()       
    return records;

def extractASantanderRecord(temp_rows): 
    temp=temp_rows[0].split('\xa0')
    temp=temp[1].split('\n')
    date=datetime.strptime(temp[0],'%d/%m/%Y')
    temp=temp_rows[2].split('\xa0') 
    temp=temp[1].split('\n')
    amount=float(temp[0])
    category=""
    temp=temp_rows[1].split('\xa0')
    temp=temp[1].split('\n')
    payee=temp[0].strip()
    address=""
    rec=record(date,payee,amount,category,address,0)
    return rec