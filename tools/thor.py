x,y,T,t=[int(i)for i in input().split()]
while 1:
    X,Y='',''
    #if t>y:Y='N' not necessary
    if T>x:X='W'
    if t<y:Y='S';t+=1   
    if T<x:X='E'
    print(Y+X)
