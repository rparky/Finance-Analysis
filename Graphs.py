import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

from startBalance import returnStartBalance


class Graphs:
    def __init__(self, records):
        self.records = records

    def balance(self):
        inout = self.records.groupby(['Date']).sum()
        balance = np.cumsum(inout['Amount'].values)
        balance += returnStartBalance()
        plt.plot(inout.index, balance)
        plt.show()

    # def regular_balance(self):
    #     inout = self.records.loc[self.records['Transfer'] == False]
    #     inout = inout.loc[self.records['Amount'] < 3000]
    #     inout = inout.groupby(['Date']).sum()
    #     balance = np.cumsum(inout['Amount'].values)
    #     balance += returnStartBalance()
    #     plt.plot(inout.index, balance)
    #     plt.show()

    def spending_grades_bar(self):
        data = self.records.loc[self.records['Transfer'] == False]
        data = data.loc[data['Amount'] < 0]
        small = -data.loc[data['Amount'] > -100, 'Amount'].values
        small = np.ceil(small/10)*10
        (unique, counts) = np.unique(small, return_counts=True)
        sns.barplot(x=unique, y=counts)
        big = -data.loc[data['Amount'] < -100, 'Amount'].values
        big = np.ceil(big / 10) * 10
        (unique, counts) = np.unique(big, return_counts=True)
        plt.figure()
        sns.barplot(x=unique, y=counts)
        plt.show()