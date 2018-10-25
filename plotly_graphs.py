#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 19:11:18 2018

Name: khalednakhleh
"""

import plotly
import plotly.figure_factory as ff
import pandas as pd

# combined_2013 file input and loacting fips data
file = pd.read_csv("combined_2013.csv")
fips = file.iloc[:, 1]

# Generating a plotly graph for diabetes, obesity for 2008 and 2013.


###################################
diabetes_2008 = file.iloc[:,4]

fig = ff.create_choropleth(fips=fips, values=diabetes_2008, \
    title = "Diabetes Percentages in 2008 - Contiguous USA", legend_title='% with diabetes')

plotly.offline.plot(fig, filename='diabetes_2008.html')

###################################
diabetes_2013 = file.iloc[:,5]

fig = ff.create_choropleth(fips=fips, values= diabetes_2013, \
     title = "Diabetes Percentages in 2013 - Contiguous USA", legend_title='% with diabetes')

plotly.offline.plot(fig, filename='diabetes_2013.html')

###################################
obesity_2008 = file.iloc[:,6]

fig = ff.create_choropleth(fips=fips, values= obesity_2008, \
     title = "Obesity Percentages in 2008 - Contiguous USA", legend_title='% obese')

plotly.offline.plot(fig, filename='obesity_2008.html')


###################################
obesity_2013 = file.iloc[:,7]

fig = ff.create_choropleth(fips=fips, values= obesity_2013, \
     title = "Obesity Percentages in 2013 - Contiguous USA", legend_title='% obese')

plotly.offline.plot(fig, filename='obesity_2013.html')


# Generating Adjust Gross Income for 2013

###################################
AGI = file.iloc[:,27]

fig = ff.create_choropleth(fips=fips, values= AGI, \
     title = "Adjust Gross Income (AGI) in 2013 - Contiguous USA", legend_title=' AGI')

plotly.offline.plot(fig, filename='agi_2013.html')
















