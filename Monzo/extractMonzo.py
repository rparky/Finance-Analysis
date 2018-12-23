# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 21:02:00 2018

@author: rpark
"""

from datetime import datetime
import classes

def extractMonzo():
    records=extractMonzoFile('Monzo/Monzo.csv')
    return records;

def extractMonzoFile(filename):
    file = open(filename, encoding="utf8")
    next(file, None) 
    records = []
    for row in file:
        rec =  extractAMonzoRecord(row)
        records.append(rec)
    return records;

def extractAMonzoRecord(row):
    data=row.split(',') 
    date=datetime.strptime(data[1],'%Y-%m-%dT%H:%M:%SZ')
    amount=float(data[2])    
    category=data[6]
    description=data[8] + ' ' + data[10]
    payee=''
    location=classes.Location(street=data[9])
    bank_details=classes.Bank_details('Monzo','Standard')
    payment_details=extractAPayment(data)
    rec=classes.Record(date,amount,category,description,payee,location,bank_details,payment_details)
    return rec;

def extractAPayment(data):
    in_out=classes.In_Out(data[2])
    payment_type='card'
    local_currency= data[5]
    local_amount=data[4]
    payment_date=datetime.strptime(data[1],'%Y-%m-%dT%H:%M:%SZ')
    pay=classes.Payment_details(in_out,payment_type,local_currency,local_amount,payment_date)
    return pay
