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
from startBalance import returnStartBalance

records=extractMonzo()
records.extend(extractSantander())
records.extend(extractTSB())

records.sort(key=lambda x: x.date_)

currentbalance=[]
currentdate=[]
balance=returnStartBalance()
for entry in records:
    balance+=entry.amount_
    currentbalance.append(balance)
    currentdate.append(entry.date_)

plt.plot(currentdate,currentbalance)
plt.ylabel('money')
plt.show()