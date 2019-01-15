# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 16:44:34 2018

@author: rpark
"""

from datetime import datetime
import classes


def extractTSB():
     records=extractClassicEnhance()
     records.extend(extractClassicPlus())
     records.extend(extractEasySaver())
     records.extend(extractISA())
     return records;

def extractClassicEnhance():
    account='ClassicEnhance'
    records=extractTSBFile('TSB/ClassicEnhance/2016A.csv',account)
    records.extend(extractTSBFile('TSB/ClassicEnhance/2016A.csv',account))
    records.extend(extractTSBFile('TSB/ClassicEnhance/2016B.csv',account))
    records.extend(extractTSBFile('TSB/ClassicEnhance/2016C.csv',account))
    records.extend(extractTSBFile('TSB/ClassicEnhance/2016E.csv',account))
    records.extend(extractTSBFile('TSB/ClassicEnhance/2017A.csv',account))
    records.extend(extractTSBFile('TSB/ClassicEnhance/2017B.csv',account))
    records.extend(extractTSBFile('TSB/ClassicEnhance/2017C.csv',account))
    records.extend(extractTSBFile('TSB/ClassicEnhance/2017D.csv',account))
    records.extend(extractTSBFile('TSB/ClassicEnhance/2017E.csv',account))
    records.extend(extractTSBFile('TSB/ClassicEnhance/2018A.csv',account))
    records.extend(extractTSBFile('TSB/ClassicEnhance/2018B.csv',account))
    records.extend(extractTSBFile('TSB/ClassicEnhance/2018C.csv',account))
    records.extend(extractTSBFile('TSB/ClassicEnhance/2018D.csv',account))
    records.extend(extractTSBFile('TSB/ClassicEnhance/2018E.csv',account))
    return records;

def extractClassicPlus():
    account='ClassicPlus'
    records=extractTSBFile('TSB/ClassicEnhance/2016A.csv',account)
    records.extend(extractTSBFile('TSB/ClassicPlus/2016A.csv',account))
    records.extend(extractTSBFile('TSB/ClassicPlus/2016B.csv',account))
    records.extend(extractTSBFile('TSB/ClassicPlus/2016C.csv',account))
    records.extend(extractTSBFile('TSB/ClassicPlus/2016D.csv',account))
    records.extend(extractTSBFile('TSB/ClassicPlus/2016E.csv',account))
    records.extend(extractTSBFile('TSB/ClassicPlus/2017A.csv',account))
    records.extend(extractTSBFile('TSB/ClassicPlus/2017B.csv',account))
    records.extend(extractTSBFile('TSB/ClassicPlus/2017C.csv',account))
    records.extend(extractTSBFile('TSB/ClassicPlus/2017D.csv',account))
    records.extend(extractTSBFile('TSB/ClassicPlus/2017E.csv',account))
    records.extend(extractTSBFile('TSB/ClassicPlus/2018A.csv',account))
    records.extend(extractTSBFile('TSB/ClassicPlus/2018B.csv',account))
    records.extend(extractTSBFile('TSB/ClassicPlus/2018C.csv',account))
    records.extend(extractTSBFile('TSB/ClassicPlus/2018D.csv',account))
    records.extend(extractTSBFile('TSB/ClassicPlus/2018E.csv',account))
    return records;

def extractEasySaver():
    account='EasySaver'
    records=extractTSBFile('TSB/EasySaver/AllTime.csv',account)
    return records;

def extractISA():
    account='ISA'
    records=extractTSBFile('TSB/ISA/AllTime.csv',account)
    return records;

def extractTSBFile(filename, account):
    file = open(filename)
    next(file, None) 
    records = []
    for row in file:  
        records.append(extractATSBRecord(row, account))

    records.reverse()       
    return records;

def extractATSBRecord(row, account): 
    data=row.split(',')
    amount=extractAmount(data)
    date=datetime.strptime(data[0],'%Y-%m-%d')
    category=''
    payee=''
    description=data[4]
    location=classes.Location()
    bank_details=classes.Bank_details('TSB', account)
    payment_details=classes.Payment_details(in_out=classes.In_Out(amount),payment_method=data[1], payment_date=date)
    rec=classes.Record(date,amount,category,description,payee,location,bank_details,payment_details)
    return rec;

def extractAmount(data):
    if len(data[5])!=0:
        amount=-float(data[5])
    else:
        amount=float(data[6])
    return amount;