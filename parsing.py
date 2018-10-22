#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 17:50:28 2018

Name: khalednakhleh

income file taken from:
    https://www.irs.gov/statistics/soi-tax-stats-county-data-2016
"""

import pandas as pd
import numpy as np

health = pd.read_csv("health_data.csv")
income = pd.read_csv("income_data.csv")


print("Initial dimensions for health and income datasets: \n")
print(health.shape)
print(income.shape)

###################################################
income_adjust = income[~((income["COUNTYFIPS"] == 0))]
income_adjust = income_adjust[~((income_adjust["COUNTYNAME"] == "Kusilvak"))]
income_adjust = income_adjust[~((income_adjust["COUNTYNAME"] == "Oglala Lakota County"))]

health_adjust = health[~((health["County"] == "Wade Hampton"))]
health_adjust = health_adjust[~((health["County"] == "Kalawao"))]
health_adjust = health_adjust[~((health_adjust["County"] == "Shannon") & (health_adjust["State"] == "SD"))]
health_adjust = health_adjust[~((health_adjust["County"] == "Bedford") & (health_adjust["State"] == "VA")& (health_adjust["PCT_DIABETES_ADULTS08"] == 12.6))]


new_index = np.arange(health_adjust.shape[0])
income_adjust.index = new_index
health_adjust.index = new_index

###################################################
print("\n--------------------------------")
print("after parsing dimensions for health and income datasets: \n")

print(income_adjust.shape)
print(health_adjust.shape)

income_adjust.to_csv("‎income_adjusted.csv", index = "Id")
health_adjust.to_csv("‎health_adjusted.csv", index = "Id")

###################################################

# Combining the parsed health and income files into one file

combined = pd.concat([health_adjust, income_adjust], axis = 1)
combined.to_csv("combined.csv", index = "Id")

print("\nParsed file dimensions: \n")
print(combined.shape)




 
 
 
 
 
