# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 16:44:34 2018

@author: rpark
"""

from datetime import datetime
from record  import record


def extractTSB():
     records=extractClassicEnhance()
     records.extend(extractClassicPlus())
     records.extend(extractEasySaver())
     records.extend(extractISA())
     return records;

def extractClassicEnhance():
    records=extractTSBFile('TSB/ClassicEnhance/2016A.csv')
    records.extend(extractTSBFile('TSB/ClassicEnhance/2016A.csv'))
    records.extend(extractTSBFile('TSB/ClassicEnhance/2016B.csv'))
    records.extend(extractTSBFile('TSB/ClassicEnhance/2016C.csv'))
    records.extend(extractTSBFile('TSB/ClassicEnhance/2016E.csv'))
    records.extend(extractTSBFile('TSB/ClassicEnhance/2017A.csv'))
    records.extend(extractTSBFile('TSB/ClassicEnhance/2017B.csv'))
    records.extend(extractTSBFile('TSB/ClassicEnhance/2017C.csv'))
    records.extend(extractTSBFile('TSB/ClassicEnhance/2017D.csv'))
    records.extend(extractTSBFile('TSB/ClassicEnhance/2017E.csv'))
    records.extend(extractTSBFile('TSB/ClassicEnhance/2018A.csv'))
    records.extend(extractTSBFile('TSB/ClassicEnhance/2018B.csv'))
    records.extend(extractTSBFile('TSB/ClassicEnhance/2018C.csv'))
    records.extend(extractTSBFile('TSB/ClassicEnhance/2018D.csv'))
    records.extend(extractTSBFile('TSB/ClassicEnhance/2018E.csv'))
    return records;

def extractClassicPlus():
    records=extractTSBFile('TSB/ClassicEnhance/2016A.csv')
    records.extend(extractTSBFile('TSB/ClassicPlus/2016A.csv'))
    records.extend(extractTSBFile('TSB/ClassicPlus/2016B.csv'))
    records.extend(extractTSBFile('TSB/ClassicPlus/2016C.csv'))
    records.extend(extractTSBFile('TSB/ClassicPlus/2016D.csv'))
    records.extend(extractTSBFile('TSB/ClassicPlus/2016E.csv'))
    records.extend(extractTSBFile('TSB/ClassicPlus/2017A.csv'))
    records.extend(extractTSBFile('TSB/ClassicPlus/2017B.csv'))
    records.extend(extractTSBFile('TSB/ClassicPlus/2017C.csv'))
    records.extend(extractTSBFile('TSB/ClassicPlus/2017D.csv'))
    records.extend(extractTSBFile('TSB/ClassicPlus/2017E.csv'))
    records.extend(extractTSBFile('TSB/ClassicPlus/2018A.csv'))
    records.extend(extractTSBFile('TSB/ClassicPlus/2018B.csv'))
    records.extend(extractTSBFile('TSB/ClassicPlus/2018C.csv'))
    records.extend(extractTSBFile('TSB/ClassicPlus/2018D.csv'))
    records.extend(extractTSBFile('TSB/ClassicPlus/2018E.csv'))
    return records;

def extractEasySaver():
    records=extractTSBFile('TSB/EasySaver/2018.csv')
    return records;

def extractISA():
    records=extractTSBFile('TSB/ISA/2018.csv')
    return records;


def extractTSBFile(filename):
    file = open(filename)
    next(file, None) 
    records = []
    for row in file:  
        records.append(extractATSBRecord(row))

    records.reverse()       
    return records;

def extractATSBRecord(row): 
    temp=row.split(',')
    date=datetime.strptime(temp[0],'%Y-%m-%d')
    category=temp[1]
    payee=temp[4]
    if len(temp[5])!=0:
        amount=-float(temp[5])
    else:
        amount=float(temp[6])
    address=""
    rec=record(date,payee,amount,category,address,0,'TSB')
    return rec