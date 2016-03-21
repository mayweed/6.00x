#!/usr/bin/python

fileTemps='julyTemps.txt'

def parseTemps(fileTemps):
    highTemps=[]
    lowTemps=[]
    fields=[]
    with open(fileTemps, 'r') as inFile:
        for line in inFile:
            #want to get read of that first
            if len(line) < 3 or not line[0].isdigit(): continue
            else:fields.append(line.split())

        for field in fields:
            highTemps.append(int(field[1]))
            lowTemps.append(int(field[2]))
        
        count=0
        while count < len(fields):
            print((highTemps[count],lowTemps[count]))
            count+=1
            
parseTemps(fileTemps)        
