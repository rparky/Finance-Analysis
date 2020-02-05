import pandas as pd

def getColumns():
     return ['Date', 'Time', 'Amount', 'Payee', 'Catagory', 'Text', 'Bank', 'Account', 'Method', 'Direction', 'Location', 'Local Currency', 'Local Amount', 'Payment Date', 'Transfer']

def newDataFrame(rows):
    return pd.DataFrame(columns=getColumns(), index=list(range(rows)) )

def newDict(rows):
    return {key: [None] * rows for key in getColumns()}