# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 21:02:00 2018

@author: rpark
"""

from datetime import datetime
from record  import record

def extractMonzo():
    records=extractMonzoFile('Monzo/Monzo.csv')
    return records;

def extractMonzoFile(filename):
    file = open(filename, encoding="utf8")
    next(file, None) 
    records = []
    balance=0
    for row in file:
        rec , balance =  extractAMonzoRecord(row, balance)
        records.append(rec)
    return records;

def extractAMonzoRecord(row, balance):
    test=row.split(',')   
    date=datetime.strptime(test[1],'%Y-%m-%dT%H:%M:%SZ')
    amount=float(test[2])
    category=test[6]
    payee=test[8][0:22].strip()
    temp=test[8][23:].split(' ')
    address=temp[0]
    balance+=amount
    rec=record(date,payee,amount,category,address,balance)
    return rec , balance;