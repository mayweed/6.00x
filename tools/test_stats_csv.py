#!/usr/bin/python

import sys
import csv
import pandas as pd

#Dont want to lose time typing and retyping.
# Should use arg instead of file name in open()'STATS_PRETS_2008_2015.csv'
# Should add csv.QUOTE_NONNUMERIC: cant convert string to float..,quoting=csv.QUOTE_NONNUMERIC)
data = []

with open(sys.argv[1], newline='') as file:
    filereader=csv.reader(file,delimiter=',',quotechar='"')
    for row in filereader:
        data.append(row)
print(data[0])
