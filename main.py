# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 19:26:57 2018

@author: rpark
"""

import matplotlib.pyplot as plt
import numpy as np

from Monzo.extractMonzo import extractMonzo
from Santander.extractSantander import extractSantander
from TSB.extractTSB import extractTSB
from Nationwide.extractNationwide import extractNationwide
from startBalance import returnStartBalance
import Utils
from datetime import datetime

records=extractMonzo()
records.extend(extractSantander())
records.extend(extractTSB())
records.extend(extractNationwide())

records.sort(key=lambda x: x.date_)

currentbalance=[]
currentdate=[]
balance=returnStartBalance()
for entry in records:
    balance+=entry.amount_
    currentbalance.append(balance)
    currentdate.append(entry.date_)    

words=[]
for entry in records:
    temp=entry.description_.split(' ')
    temp2=[]
    for element in temp:
        a = element.strip()
        temp2.extend(a.split(','))
    
    words.extend(temp2)

words = list(filter(None, words))
words.sort()
    
lesswords = list(dict.fromkeys(words))
lesswords.sort()

dates=[]
numbers=[]
probablynumber=[]
cash=[]
stillwords=[]
for word in lesswords:
    if Utils.isDateTime(word):
        dates.append(datetime.strptime(word,'%d-%m-%Y'))
    elif Utils.isDateTime2(word):
        dates.append(datetime.strptime(word,'%Y-%m-%d'))
    elif Utils.isfloat(word):
        numbers.append(float(word))
    elif '£' in word:
        cash.append(word)
    elif Utils.isfloat(word[0]):
        probablynumber.append(word)
    else:
        stillwords.append(word)

#first remove dates
#then remove money
# then remove other random numbers

plt.plot(currentdate,currentbalance)
plt.ylabel('money')
plt.show()