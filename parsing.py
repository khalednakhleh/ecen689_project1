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


print("Initial dimensions for health and income datasets: \n")
print(health.shape)
print(income.shape)


print("\n\n\n--------------------------------")
print("after parsing dimensions for health and income datasets: \n")

income_adjust = income.drop(income[income.COUNTYFIPS == 0].index)
income_adjust = income_adjust.drop(income_adjust[income_adjust.COUNTYNAME == "Kusilvak"].index)
income_adjust = income_adjust.drop(income_adjust[income_adjust.COUNTYNAME == "Oglala Lakota County"].index)

print(income_adjust.shape)

health_adjust = health.drop(health[health.County == "Wade Hampton"].index)
health_adjust = health_adjust.drop(health_adjust[health_adjust.County == "Kalawao"].index)
health_adjust = health_adjust[~((health_adjust["County"] == "Shannon") & (health_adjust["State"] == "SD"))]
health_adjust = health_adjust[~((health_adjust["County"] == "Bedford") & (health_adjust["State"] == "VA")& (health_adjust["PCT_DIABETES_ADULTS08"] == 12.6))]

health_adjust.index += 1
print(health_adjust.shape)

###################################################

income_adjust.to_csv("‎income_adjusted.csv")
health_adjust.to_csv("‎health_adjusted.csv")
 
###################################################


# Combining the parsed health and income files into one file


combined = pd.concat([health_adjust, income_adjust], axis = 1)
combined.to_csv("combined.csv")

print(combined.shape)
















 
 
 
 
 