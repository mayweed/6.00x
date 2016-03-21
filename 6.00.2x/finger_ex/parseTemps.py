#!/usr/bin/python

import pylab

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
            
def producePlot(highTemps,lowTemps):
    diffTemps=[]
    count=0
    while count < len(highTemps):
        diffTemps.append(highTemps[count]-lowTemps[count])
        count+=1
    # with numpy: diffTemps = list(np.array(highTemps) - np.array(lowTemps))
    # very nice!!! should learn numpy a bit ^^
    pylab.plot(range(1,32),diffTemps)
    pylab.title('Day by Day Ranges in Temperature in Boston in July 2012')
    pylab.xlabel('Days')
    pylab.ylabel('Temperature Ranges')
    pylab.show()

high,low=parseTemps(fileTemps)
producePlot(high,low)
