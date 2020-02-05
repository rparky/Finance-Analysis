import numpy as np

class PreProcessing:
    def __init__(self, records):
        self.records = records

    def identify_transfers(self):
        self.records['Transfer'] = False
        dates = self.records.Date.unique()
        for date in dates:
            days_records = self.records.loc[self.records['Date'] == date]
            non_transfers = days_records.loc[days_records['Transfer'] == False]
            money_in = non_transfers.loc[non_transfers['Amount'] > 0]
            for index, row in money_in.iterrows():
                value = -row['Amount']
                for index2, row2 in non_transfers.iterrows():
                    value2 = row2['Amount']
                    if value == value2:
                        self.records.at[index, 'Transfer'] = True
                        self.records.at[index2, 'Transfer'] = True
                        non_transfers = days_records.loc[days_records['Transfer'] == False]
                        break
