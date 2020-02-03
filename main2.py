# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 19:35:32 2019

@author: rpark

"""

from extractSantander2 import extractSantander
from extractMonzo2 import extractMonzo
from extractNationwide2 import extract_nationwide
from extractTSB2 import extract_TSB
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

santander = extractSantander()
monzo = extractMonzo()
nationwide = extract_nationwide()
TSB = extract_TSB()
records = pd.concat([santander, monzo, nationwide, TSB])
records = records.sort_values(by=['Date'])
# sns.lineplot(y='Amount', x='Date', data=records)
inout = records.groupby(['Date']).sum()
balance = np.cumsum(inout.values)
plt.plot(inout.index, balance)
plt.show()
# test = 1