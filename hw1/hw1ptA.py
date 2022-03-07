#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 16:30:50 2021

@author: sydneylance
"""

#user input
annual_salary = float(input("Enter your starting annual salary:"))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal:"))
total_cost = float(input("Enter the cost of your dream home:"))

portion_down_payment = .25*total_cost
current_savings = 0
monthly_salary = annual_salary/12
r = .04
months = 0

#adds increase in funds to current savings and counts months
while current_savings < portion_down_payment:
    current_savings += (portion_saved*monthly_salary)+(current_savings*r/12)
    months += 1
    
print(months)









