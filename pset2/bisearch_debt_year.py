#!/usr/bin/python

"""
Those 2 values for testing purposes only
Res=90325.03
"""
balance=999999
annualInterestRate=0.18

remainingBalance=balance
monthlyInterestRate=annualInterestRate/12.0

lower_bound=round((balance/12.0),2)
upper_bound=round(balance *((1 + monthlyInterestRate)**12)/12.0,2)
mid=lower_bound+(upper_bound-lower_bound)/2.0
print(mid)
#compare it to remaining balance at the end of the year
# si l'ecart entre remainingbalance et 0 est > à epsilon
epsilon=0.1

def remaining_balance(owed_sum,monthlyPayment):
    unpaid_balance= owed_sum - monthlyPayment
    x=unpaid_balance + (monthlyInterestRate*unpaid_balance)
    return x

#def binarySearch(low,high):


monthlyPayment=mid
#while remainingBalance != 0:
#TEST
x=0
while x < 20:
#there is a problem: it's infinite loop but as if monthlyPayment never
#gets updated (it stays at 91484 while remainingBalance is around :15000)
    remainingBalance=balance
    if remainingBalance-epsilon < epsilon: 
        upper_bound=mid
        mid=lower_bound+(upper_bound-lower_bound)/2.0
        monthlyPayment=mid
        remainingBalance=balance
        for i in range(1,13):
            owed=remaining_balance(remainingBalance,monthlyPayment)
            print(i,owed,monthlyPayment)
            #should update that value between each iteration
            #unless infinite loop...
            remainingBalance=owed
        remainingBalance=owed
    if remainingBalance-epsilon > epsilon:
        lower_bound=mid
        #upper_bound=
        mid=lower_bound+(upper_bound-lower_bound)/2.0
        monthlyPayment=mid
        remainingBalance=balance
        for i in range(1,13):
            owed=remaining_balance(remainingBalance,monthlyPayment)
            print(i,owed,monthlyPayment)
            #should update that value between each iteration
            #unless infinite loop...
            remainingBalance=owed
    #if what you owed is > to 0 loop again oki?
    remainingBalance=owed
    upper_bound=mid
    mid=lower_bound+(upper_bound-lower_bound)/2.0
    monthlyPayment=mid
    x+=1

#    print("Remaining Balance: ",owed)

#print("Lowest payment: ",monthlyPayment)
