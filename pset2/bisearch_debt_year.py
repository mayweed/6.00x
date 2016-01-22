#!/usr/bin/python

"""
Those 2 values for testing purposes only
"""
balance=3101
annualInterestRate=0.18

owed_sum=balance
monthlyInterestRate=annualInterestRate/12.0
monthlyPayment=10 

def remaining_balance(owed_sum):
    unpaid_balance= owed_sum - monthlyPayment
    x=unpaid_balance + (monthlyInterestRate*unpaid_balance)
    return round(x)

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
