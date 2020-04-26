from extractSantander import extract_santander
from extractMonzo import extract_monzo
from extractNationwide import extract_nationwide
from extractTSB import extract_TSB
import pandas as pd

from PreProcessing import PreProcessing
from Graphs import Graphs

santander = extract_santander()
monzo = extract_monzo()
nationwide = extract_nationwide()
TSB = extract_TSB()
records = pd.concat([santander, monzo, nationwide, TSB], ignore_index=True)
preprocessing = PreProcessing(records)
preprocessing.identify_transfers()

records = preprocessing.records.sort_values(by=['Date'])
graphs = Graphs(records)

test = records.loc[records['Transfer'] == False]
test = test.loc[test['Amount'] > 0]

graphs.balance()
test = 1
