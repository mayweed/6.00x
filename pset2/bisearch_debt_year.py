#!/usr/bin/python

"""
Those 2 values for testing purposes only
"""
balance=999999
annualInterestRate=0.18

owed_sum=balance
monthlyInterestRate=annualInterestRate/12.0
monthlyPayment=10.0 

lower_bound=round((balance/12.0),2)
print(lower_bound)
upper_bound=round(balance *((1 + monthlyInterestRate)**12)/12.0,2)
print(upper_bound)
mid=lower_bound+(upper_bound-lower_bound)/2
print(mid)

def remaining_balance(owed_sum):
    unpaid_balance= owed_sum - monthlyPayment
    x=unpaid_balance + (monthlyInterestRate*unpaid_balance)
    return round(x,2)

def calculate_balance(owed_sum,monthlyPayment):
    for i in range(1,13):
        #print("MonthlyPayment ",monthlyPayment)
        x= remaining_balance(owed_sum)
        #print("Month/remB ",i,x)
        owed_sum=x
    return owed_sum

x=calculate_balance(owed_sum,monthlyPayment)
while x >= 0:
    owed_sum=balance
    monthlyPayment += 10
    x=calculate_balance(owed_sum,monthlyPayment)

print("Lowest payment: ",monthlyPayment)
