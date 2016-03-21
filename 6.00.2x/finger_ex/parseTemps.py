#!/usr/bin/python

fileTemps='julyTemps.txt'

def parseTemps(fileTemps):
    highTemps=[]
    lowTemps=[]
    with open(fileTemps, 'r') as inFile:
        for line in inFile:
            #want to get read of that first
            fields=line.split()

            if len(line) < 3 or not line[0].isdigit(): 
                continue
            else: 
                highTemps.append(int(fields[1]))
                lowTemps.append(int(fields[2]))
        
        # A tuple of the two lists!!
        return(highTemps,lowTemps)
            
parseTemps(fileTemps)        
