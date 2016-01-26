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

def remaining_balance(owed_sum,monthlyPayment):
    unpaid_balance= owed_sum - monthlyPayment
    x=unpaid_balance + (monthlyInterestRate*unpaid_balance)
    return x

monthlyPayment=mid
#x=calculate_balance(owed_sum,monthlyPayment)
#You begin with a neat balance
remainingBalance=balance
while remainingBalance > 0:
    remainingBalance=balance
    monthlyPayment=mid
    for i in range(1,13):
        owed=remaining_balance(remainingBalance,monthlyPayment)
        print(i,owed,monthlyPayment)
        #should update that value between each iteration
        #unless infinite loop...
        remainingBalance=owed
        if owed - epsilon <0: 
            upper_bound=mid
            mid=lower_bound+(upper_bound-lower_bound)/2.0
            monthlyPayment=mid
            remainingBalance=balance
            for i in range(1,13):
                owed=remaining_balance(remainingBalance,monthlyPayment)
                print(i,owed,monthlyPayment)
                #should update that value between each iteration
                #unless infinite loop...
                remainingBalance=owed
        if owed-epsilon > epsilon:
            lower_bound=mid
            mid=lower_bound+(upper_bound-lower_bound)/2.0
            monthlyPayment=mid
            remainingBalance=balance
            for i in range(1,13):
                owed=remaining_balance(remainingBalance,monthlyPayment)
                print(i,owed,monthlyPayment)
                #should update that value between each iteration
                #unless infinite loop...
                remainingBalance=owed


    #if what you owed is > to 0 loop again oki?
    remainingBalance=owed
    print(owed)

print("Lowest payment: ",monthlyPayment)
