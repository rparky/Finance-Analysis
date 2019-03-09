# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 20:45:40 2019

@author: rpark
"""

import pandas as pd

def getColumns():
     return ['Date', 'Amount', 'Payee' , 'Catagory', 'Text', 'Bank', 'Account', 'Method', 'Direction', 'Location', 'Local Currency', 'Local Amount', 'Payment Date']

def newDataFrame(rows):
    return pd.DataFrame(columns=getColumns(), index=list(range(rows)) )

def newDict(rows):
    return {key: [None] * rows for key in getColumns()}

class Location (object):
    def __init__(self, street='',city='',country='',postcode=''):
        self.street_=street
        self.city_=city
        self.country_=country
        self.postcode_=postcode