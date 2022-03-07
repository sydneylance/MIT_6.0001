#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 14:23:15 2021

@author: sydneylance
"""

#user input
annual_salary = float(input("Enter your starting annual salary:"))

#define variables
total_cost = 1000000
semi_annual_raise = .07
current_savings = 0
epsilon = 100
steps = 0
low = 0
high = 10000
guess = (high+low) // 2
portion_down_payment = .25
down_payment = portion_down_payment*total_cost
monthly_salary = annual_salary/12
r = .04
month = 0


while abs(down_payment - current_savings) >= epsilon :
    
    current_savings = 0
    rate = guess/10000
    annual_salary_forloop = annual_salary
    
    #calculating amount saved in 36 months
    for month in range(37):
        if month % 6 == 0 and month > 0: #for every sixth month, raises salary by user input semi_annual_raise
                annual_salary_forloop  +=  annual_salary_forloop * semi_annual_raise
        monthly_salary = annual_salary_forloop / 12
        current_savings += (r/12 * current_savings) + (rate * monthly_salary)
           
    #bisection search
    if current_savings < down_payment :
            low = guess
    else:
        high = guess
    guess = (high + low) // 2
    steps += 1
    
    #log2 of 10000 is a little more than 13, so 13 is the max
    if steps > 13:
        break
    
# #output
if steps > 13 :
    print("It is not possible to save for the down payment in 36 months")

else:
    print("Best savings rate:",rate)
    print("Steps in bisection search:", steps)