# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 20:45:36 2018

@author: rpark
"""
import numpy as np

class Location (object):
    def __init__(self, street='',city='',country='',postcode=''):
        self.street_=street
        self.city_=city
        self.country_=country
        self.postcode_=postcode
    
class Bank_details(object):
    def __init__(self,bank,account):
        self.bank_=bank
        self.account_=account

class Payment_details:
    def __init__(self,in_out='', payment_method='', local_currency='', local_amount='', payment_date=''):
        self.in_out_=in_out
        self.payment_method_=payment_method
        self.local_currency_=local_currency
        self.local_amount_=local_amount
        self.payment_date_=payment_date

class Record(object):
    def __init__(self,date,amount,category='',description='',payee='',location='',bank_details='',payment_details=''):
        self.date_=date
        self.payee_=payee
        self.amount_=amount
        self.category_=category
        self.description_=description
        self.bank_details_=bank_details
        self.payment_details_=payment_details
        self.location_=location
        
def In_Out(amount):
    return bool(np.sign(float(amount)));        
        