#!/usr/bin/python

balance=4842
annualInterestRate=0.2
monthlyPaymentRate=0.04
monthlyInterestRate=annualInterestRate/12.0
paid=[]

def balanceAfterInterest(balance,monthlyInterestRate):
    unpaid_balance= balance - miniMonthlyPayment
    interest=unpaid_balance + (monthlyInterestRate*unpaid_balance)
    return round(interest,2)

for i in range(1,13):
    miniMonthlyPayment=round(balance*monthlyPaymentRate,2)
    paid.append(miniMonthlyPayment)
    print("Month:",i)
    print("Minimum Monthly Payment:",miniMonthlyPayment)
    print("Remaining balance:",balanceAfterInterest(balance,monthlyInterestRate))
    balance=balanceAfterInterest(balance,monthlyInterestRate)
