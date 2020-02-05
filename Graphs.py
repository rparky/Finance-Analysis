import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from startBalance import returnStartBalance

class Graphs:
    def __init__(self, records):
        self.records = records

    def Balance(self):
        inout = self.records.groupby(['Date']).sum()
        balance = np.cumsum(inout['Amount'].values)
        balance += returnStartBalance()
        plt.plot(inout.index, balance)
        plt.show()