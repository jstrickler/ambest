#!/usr/bin/env python
import pandas as pd

df = pd.read_csv('DATA/airport_boardings.csv', thousands=',', index_col=1)

print(df.head())
print()

print(df.loc['DFW':'LAX','2010 Total'])
