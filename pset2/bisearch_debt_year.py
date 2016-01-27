#!/usr/bin/python

"""
Those 2 values for testing purposes only
Res=90325.03
"""
balance=999999
annualInterestRate=0.18

epsilon=0.2
owed_sum=balance
monthlyInterestRate=annualInterestRate/12.0
lower_bound=round((balance/12.0),2)
upper_bound=round(balance *((1 + monthlyInterestRate)**12)/12.0,2)
mid=lower_bound+(upper_bound-lower_bound)/2.0
monthlyPayment=mid

def remaining_balance(owed_sum):
    """
        Yields the remaining balance with interest after one
        monthlyPayment
    """
    unpaid_balance= owed_sum - monthlyPayment
    x=unpaid_balance + (monthlyInterestRate*unpaid_balance)
    return x

def calculate_balance(owed_sum,monthlyPayment):
    """
        Yields the remaining balance after 12 months of payment
    """
    for i in range(1,13):
        x= remaining_balance(owed_sum)
        owed_sum=x
    return owed_sum

remainingBalance=balance
while abs(remainingBalance) >= epsilon :
    owed_sum=balance
    monthlyPayment=lower_bound+(upper_bound-lower_bound)/2.0
    remainingBalance=calculate_balance(owed_sum,monthlyPayment)

    if remainingBalance < 0: 
        upper_bound=monthlyPayment
        
    if remainingBalance > 0: 
        lower_bound=monthlyPayment

print("Lowest payment: ",round(monthlyPayment,2))
