# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 20:45:36 2018

@author: rpark
"""

class record(object):
    def __init__(self,date,payee,amount,category,address,balance,account):
        self.date_=date
        self.payee_=payee
        self.amount_=amount
        self.category_=category
        self.address_=address
        self.balance_=balance
        self.account_=account
        
        