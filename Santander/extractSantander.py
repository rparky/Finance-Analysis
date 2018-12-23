# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 21:23:28 2018

@author: rpark
"""

from datetime import datetime
import classes

def extractSantander():
     records=extractSantanderCurrent()
     records.extend(extractSantanderSavings())
     return records;

def extractSantanderCurrent():
    account='current'
    records=extractSantanderFile('Santander/Current/SantanderCurrent2012.txt',account)
    records.extend(extractSantanderFile('Santander/Current/SantanderCurrent2013.txt',account))
    records.extend(extractSantanderFile('Santander/Current/SantanderCurrent2014.txt',account))
    records.extend(extractSantanderFile('Santander/Current/SantanderCurrent2015.txt',account))
    records.extend(extractSantanderFile('Santander/Current/SantanderCurrent2016.txt',account))
    records.extend(extractSantanderFile('Santander/Current/SantanderCurrent2017.txt',account))
    records.extend(extractSantanderFile('Santander/Current/SantanderCurrent2018.txt',account))
    return records;

def extractSantanderSavings():
    account='Savings'
    records=extractSantanderFile('Santander/Savings/SantanderSavings2017.txt',account)
    records.extend(extractSantanderFile('Santander/Savings/SantanderSavings2018.txt',account))
    return records;

def extractSantanderFile(filename,account):
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
            records.append(extractASantanderRecord(temp_rows,account))
            temp_rows= []
    
    records.append(extractASantanderRecord(temp_rows,account))
    records.reverse()       
    return records;

def extractASantanderRecord(temp_rows, account): 
    temp=temp_rows[0].split('\xa0')
    temp=temp[1].split('\n')
    date=datetime.strptime(temp[0],'%d/%m/%Y')
    temp=temp_rows[2].split('\xa0') 
    temp=temp[1].split('\n')
    amount=float(temp[0])
    category=''
    description=temp_rows[1]
    payee=''
    location=classes.Location()
    bank_details=classes.Bank_details('Santander',account)
    payment_details=classes.Payment_details(in_out=classes.In_Out(amount),payment_date=date)
    rec=classes.Record(date,amount,category,description,payee,location,bank_details,payment_details)
    return rec;