#!/usr/bin/python

"""
Those values shouldn't be specified
Here for test purposes only
balance=3568
annualInterestRate=0.18
monthlyPaymentRate=0.05
"""
monthlyInterestRate=annualInterestRate/12.0
paid=[]

def balanceAfterInterest(balance,monthlyInterestRate):
    unpaid_balance= balance - miniMonthlyPayment
    interest=unpaid_balance + (monthlyInterestRate*unpaid_balance)
    return round(interest,2)

for i in range(1,13):
    miniMonthlyPayment=round(balance*monthlyPaymentRate,2)
    paid.append(miniMonthlyPayment)
    if i < 12:
        print("Month:",i)
        print("Minimum Monthly Payment:",miniMonthlyPayment)
        print("Remaining balance:",balanceAfterInterest(balance,monthlyInterestRate))

    if i==12:
        print("Month:",i)
        print("Minimum Monthly Payment:",miniMonthlyPayment)
        print("Remaining balance:",balanceAfterInterest(balance,monthlyInterestRate))
        print("Total paid:",round(sum(paid),2))
        print("Remaining balance:",balanceAfterInterest(balance,monthlyInterestRate))
    balance=balanceAfterInterest(balance,monthlyInterestRate)
