#!/usr/bin/python

balance=3329
annualInterestRate=0.18
monthlyInterestRate=annualInterestRate/12.0

#That's what I must guess(cf upper bound)
#Should decrease that inside the loop
monthlyPayment= round((balance * (1 + monthlyInterestRate))/12) 
print(round(monthlyPayment))
remaining_balance=balance

def balanceAfterInterest(balance,monthlyInterestRate):
    unpaid_balance= balance - monthlyPayment
    interest=unpaid_balance + (monthlyInterestRate*unpaid_balance)
    return round(interest,2)

#loop condition not good
while balanceAfterInterest(remaining_balance,monthlyInterestRate) > 0:
    for i in range(1,11):
        month=i
        print("Month:",i)
        print("Minimum Monthly Payment:",monthlyPayment)
        print("Remaining balance:",balanceAfterInterest(balance,monthlyInterestRate))
        remaining_balance=balanceAfterInterest(balance,monthlyInterestRate)
        if remaining_balance <=0 :break
    monthlyPayment-=10
    #go for another one with diff payment but same original balance
remaining_balance=balance
