# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 20:45:31 2019

@author: rpark
"""

from datetime import datetime

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

def isDateTime(value):
  try:
    datetime.strptime(value,'%d-%m-%Y')
    return True
  except ValueError:
    return False

def isDateTime2(value):
  try:
    datetime.strptime(value,'%Y-%m-%d')
    return True
  except ValueError:
    return False