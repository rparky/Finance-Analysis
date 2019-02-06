# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 21:02:00 2018

@author: rpark
"""

from datetime import datetime
import classes

def extractNationwide():
    records=extractNationwideFile('Nationwide/FlexclusiveSaver/2018.csv', 'FlexclusiveSaver')
    records.extend(extractNationwideFile('Nationwide/FlexiDirect/2018.csv', 'FlexiDirect'))
    records.extend(extractNationwideFile('Nationwide/ISA/2018.csv', 'ISA'))
    return records;

def extractNationwideFile(filename, account):
    file = open(filename)
    next(file, None)
    next(file, None) 
    next(file, None) 
    next(file, None) 
    next(file, None) 
    records = []
    for row in file:
        rec =  extractANationwideRecord(row, account)
        records.append(rec)
    return records;

def extractANationwideRecord(row, account):
    row2=row.replace('"','')
    data=row2.split(',') 
    date=datetime.strptime(data[0],'%d %b %Y')
    amount=getAmount(data[3],data[4])    
    category=''
    description=data[2]
    payee=''
    location=classes.Location()
    bank_details=classes.Bank_details('Nationwide',account)
    payment_details=payment_details=classes.Payment_details(in_out=classes.In_Out(amount),payment_method=data[1], payment_date=date)
    rec=classes.Record(date,amount,category,description,payee,location,bank_details,payment_details)
    return rec;

def getAmount(in_, out_):
    val=0
    if len(in_)!=0:
        val+=float(in_[1:])
    if len(out_)!=0:
        val-=float(out_[1:])
    return val