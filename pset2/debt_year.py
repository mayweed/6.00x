#!/usr/bin/python

balance=4773
annualInterestRate=0.2

owed_sum=balance

def roundupdown(num):
    #Must be a multiple of ten
    if num%10 !=0:
        if num%10 > 5:
            #round up
            num += (10 - (num%10))
        elif num%10 < 5:
            #round down
            num-=(num%10)
    return round(num)

#MATHS
monthlyInterestRate=annualInterestRate/12.0
monthlyPayment= roundupdown((balance * (1 + monthlyInterestRate))/12) 

def remaining_balance(owed_sum):
    unpaid_balance= owed_sum - monthlyPayment
    x=unpaid_balance + (monthlyInterestRate*unpaid_balance)
    return round(x)

def calculate_balance(owed_sum,monthlyPayment):
    for i in range(1,11):
        print("balance ",owed_sum)
        print("MonthlyPayment ",monthlyPayment)
        x= remaining_balance(owed_sum)
        print("Month/remB ",i,x)
        owed_sum=x
    return owed_sum

x=calculate_balance(owed_sum,monthlyPayment)
while x > 0:
    owed_sum=balance
    monthlyPayment += 10
    x=calculate_balance(owed_sum,monthlyPayment)

print(monthlyPayment)
