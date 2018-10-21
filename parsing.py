#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 17:50:28 2018

Name: khalednakhleh

file taken from:
    https://www.irs.gov/statistics/soi-tax-stats-county-data-2016
"""

import pandas as pd
import numpy as np

health = pd.read_csv("health_data.csv")
income = pd.read_csv("good_income_data.csv")
combined = pd.read_csv("health_income_data.csv")

print(income.head())

print(income.iloc[1, 3])
print(health.iloc[0, 2])

print(health.shape)
print(income.shape)


print(np.count_nonzero(income.iloc[:, 2] == 0))
"""
if health.iloc[0, 2] + " County" == income.iloc[1, 3]:
    combined.iloc[]



q = 0

while q < health.shape[0]:
    
    i = 0
    
    while i < income.shape[0]:
        
        if health.iloc[q, 2] + " County" == income.iloc[i, 3]:
            combined.iloc
        
        i = i + 1
        
 
    q = q + 1
    
"""   