#!/usr/bin/python

import sys
import csv

#Dont want to lose time typing and retyping.
# Should use arg instead of file name in open()'STATS_PRETS_2008_2015.csv'
# Should add csv.NONNUMERIC: cant convert string to float..
with open(sys.argv[1], newline='') as file:
    filereader=csv.reader(file,delimiter=',',quotechar='"',quoting=csv.QUOTE_NONNUMERIC)
    for row in filereader:
        print(row)
