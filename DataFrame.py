import pandas as pd


def get_columns():
     return ['Date', 'Time', 'Amount', 'Payee', 'Catagory', 'Text', 'Bank', 'Account', 'Method', 'Direction', 'Location', 'Local Currency', 'Local Amount', 'Payment Date', 'Transfer']


def new_data_frame(rows):
    return pd.DataFrame(columns=get_columns(), index=list(range(rows)))


def new_dict(rows):
    return {key: [None] * rows for key in get_columns()}