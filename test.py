# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 19:26:57 2018

@author: rpark
"""

import matplotlib.pyplot as plt
import numpy as np

from Monzo.extractMonzo import extractMonzo
from Santander.extractSantander import extractSantander

records=extractMonzo()
records.extend(extractSantander())

records.sort(key=lambda x: x.date_)

balance=457.66
for entry in records:
    balance+=entry.amount_
    entry.balance_=balance

plt.plot([o.date_ for o in records],[o.balance_ for o in records])
plt.ylabel('money')
plt.show()