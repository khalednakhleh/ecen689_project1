#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 17:50:28 2018

Name: khalednakhleh

file taken from:
    https://www.irs.gov/statistics/soi-tax-stats-county-data-2016
"""

import pandas as pd


health = pd.read_csv("health_data.csv")
income = pd.read_csv("income_data.csv")




print(health.shape)


income_adjust = income.drop(income[income.COUNTYFIPS == 0].index)

print(income_adjust.shape)

income_adjust.to_csv("‎income_adjusted.csv")

name = []

q = 0

while q < health.shape[0]:
    
    value = 0
    i = 0  
    
    while i < income_adjust.shape[0]:
            
        if health.iloc[q, 2] or health.iloc[q, 2] + " County" == income_adjust.iloc[i, 3]:
            value = 1
            
        i = i + 1
        
    if value == 0:
        name.append(health.iloc[q, 2])
     
    q = q + 1
    
print(name)
 
 
 
 
 
 
 