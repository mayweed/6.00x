#!/usr/bin/python

balance=3568
annualInterestRate=0.18
monthlyInterestRate=annualInterestRate/12.0

#That's what I must guess(cf upper bound)
#Should decrease that inside the loop
monthlyPayment= (balance * (1 + monthlyInterestRate)12)/12 
print(monthlyPayment)

# to check i I've paid everything or not
paid=[]

def balanceAfterInterest(balance,monthlyInterestRate):
    unpaid_balance= balance - miniMonthlyPayment
    interest=unpaid_balance + (monthlyInterestRate*unpaid_balance)
    return round(interest,2)


while sum(paid)>0: #monthlyPayment * 10 > 0 
    for i in range(1,11):
        paid.append(monthlyPayment)
        print("Month:",i)
        print("Minimum Monthly Payment:",monthlyPayment)
        print("Remaining balance:",balanceAfterInterest(balance,monthlyInterestRate))
        balance=balanceAfterInterest(balance,monthlyInterestRate)
    monthlyPayment-=10



