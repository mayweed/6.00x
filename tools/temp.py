import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(raw_input()) # the number of temperatures to analyse
temps = raw_input() # the n temperatures expressed as integers ranging from -273 to 5526
# no temps, print 0
if not temps:
        print(0)
            
# Set fields
data=[]
data= temps.split()
infra_list=[]
supra_list=[]

# Fill the lists
for i in range(len(data)):
    if int(data[i]) < 0:
        infra_list.append(int(data[i]))
    if int(data[i]) > 0:
        supra_list.append(int(data[i]))

# no empty lists
if infra_list and supra_list:
    minus= max(infra_list)        
    supra= min(supra_list)
if abs(minus) == supra:
    print(supra)
elif abs(minus) < supra:
    print(minus)
else:
    print(supra)
elif not infra_list or not supra_list:
    if not infra_list:
        print(min(supra_list))
    if not supra_list:
        print(max(infra_list))
