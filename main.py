from extractSantander import extractSantander
from extractMonzo import extractMonzo
from extractNationwide import extract_nationwide
from extractTSB import extract_TSB
import pandas as pd

from PreProcessing import PreProcessing
from Graphs import Graphs

santander = extractSantander()
monzo = extractMonzo()
nationwide = extract_nationwide()
TSB = extract_TSB()
records = pd.concat([santander, monzo, nationwide, TSB], ignore_index=True)
preprocessing = PreProcessing(records)
preprocessing.identify_transfers()

records = preprocessing.records.sort_values(by=['Date'])
graphs = Graphs(records)
graphs.Balance()
test = 1