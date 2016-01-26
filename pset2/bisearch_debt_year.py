#!/usr/bin/python

"""
Those 2 values for testing purposes only
Res=90325.03
"""
balance=999999
annualInterestRate=0.18

owed_sum=balance
monthlyInterestRate=annualInterestRate/12.0

lower_bound=round((balance/12.0),2)
upper_bound=round(balance *((1 + monthlyInterestRate)**12)/12.0,2)
mid=lower_bound+(upper_bound-lower_bound)/2.0

#compare it to remaining balance at the end of the year
# si l'ecart entre remainingbalance et 0 est > à epsilon
epsilon=0.1

def remaining_balance(owed_sum):
    unpaid_balance= owed_sum - monthlyPayment
    x=unpaid_balance + (monthlyInterestRate*unpaid_balance)
    return x

def calculate_balance(owed_sum,monthlyPayment):
    for i in range(1,13):
        print("MonthlyPayment ",monthlyPayment)
        x= remaining_balance(owed_sum)
        print("Month/remB ",i,x)
        owed_sum=x
    return owed_sum

monthlyPayment=mid
x=calculate_balance(owed_sum,monthlyPayment)
#while x - 0 > epsilon:
#    owed_sum=balance
#    x=calculate_balance(owed_sum,monthlyPayment)
if x < epsilon:
    owed_sum=balance
    upper_bound=mid
    mid=lower_bound+(upper_bound-lower_bound)/2.0
    monthlyPayment=mid
    x=calculate_balance(owed_sum,monthlyPayment)
    """
    if x > epsilon:
        owed_sum=balance
        low=mid
        mid=lower_bound+(upper_bound-lower_bound)/2.0
        monthlyPayment=mid
        x=calculate_balance(owed_sum,monthlyPayment)
"""
print("Lowest payment: ",monthlyPayment)
