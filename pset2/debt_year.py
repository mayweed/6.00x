#!/usr/bin/python

balance=3329
annualInterestRate=0.18
monthlyInterestRate=annualInterestRate/12.0

#That's what I must guess(cf upper bound)
#Should decrease that inside the loop
monthlyPayment= round((balance * (1 + monthlyInterestRate))/12) 
print(round(monthlyPayment))

def balanceAfterInterest(balance,monthlyInterestRate):
    unpaid_balance= balance - monthlyPayment
    interest=unpaid_balance + (monthlyInterestRate*unpaid_balance)
    return round(interest,2)

#loop condition not good
while balanceAfterInterest(balance,monthlyInterestRate) > 0:
    for i in range(1,11):
        print("Month:",i)
        print("Minimum Monthly Payment:",monthlyPayment)
        print("Remaining balance:",balanceAfterInterest(balance,monthlyInterestRate))
        balance=balanceAfterInterest(balance,monthlyInterestRate)
    monthlyPayment-=10
