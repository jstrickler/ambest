#!/usr/bin/env python
import csv
from pprint import pprint

INPUT_FILE = 'DATA/airport_boardings.csv'


mydata = {}

with open(INPUT_FILE) as ab_in:
    rdr = csv.DictReader(ab_in)
    for row in rdr:
        key = row['Code']  # get ATL, LAX, etc
        del row['Code']
        mydata[key] = dict(row)


pprint(mydata)
print()
print(mydata['TPA']['2011 Rank'])

# for K, V in sorted(DICT.items()):
#    ...
for code, data_dict in mydata.items():
    print(code, data_dict['2010 Total'])
