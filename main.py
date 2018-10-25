#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 16:40:47 2018

Name: khalednakhleh

Run the file parsing.py first to obtain the file combined.csv
"""
import plotly
import plotly.figure_factory as ff
import pandas as pd
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import polyfit
from sklearn.linear_model import LinearRegression as lr

def plotly_graphs(file):


    # combined_2013 file input and loacting fips data
    
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
    

def main():
    
    health_income = pd.read_csv("combined_2013.csv")
    
    print(health_income.shape)
    
    # Grabbing the data vectors
    diabetes_2008 = health_income.iloc[:, 4]
    diabetes_2013 = health_income.iloc[:, 5]
    obesity_2008 = health_income.iloc[:, 6]
    obesity_2013 = health_income.iloc[:, 7] 
    agi = health_income.iloc[:, 27] 
    wages = health_income.iloc[:, 30] 
    
    plt.figure(1)
    plt.scatter(diabetes_2013, obesity_2013, marker = "o")
    plt.title("Obesity percentage vs. diabetes percentage in 2013")
    plt.xlabel("% diabetes")
    plt.ylabel("% obesity")
    plt.grid()
    plt.savefig("obesity_diabetes.png")
    plt.show()
    
    plt.figure(2)
    plt.scatter(obesity_2013, agi)
    plt.title("Adjusted Gross Income (AGI) vs. obesity percentage in 2013")
    plt.xlabel("% obesity")
    plt.ylabel("AGI")
    plt.grid()
    plt.savefig("agi_obesity.png")
    plt.show() 
    
    plt.figure(3)
    plt.scatter(obesity_2013, wages)
    plt.title("Wages vs. obesity percentage in 2013")
    plt.xlabel("% obesity")
    plt.ylabel("Wages")
    plt.grid()
    plt.savefig("wages_obesity.png")
    plt.show()   
    
    plt.figure(4)
    plt.scatter(diabetes_2013, agi)
    plt.title("Adjusted Gross Income (AGI) vs. diabetes percentage in 2013")
    plt.xlabel("% diabetes")
    plt.ylabel("AGI")
    plt.grid()
    plt.savefig("agi_diabetes.png")
    plt.show()   
    
    plt.figure(5)
    plt.scatter(diabetes_2013, wages)
    plt.title("Wages vs. diabetes percentage in 2013")
    plt.xlabel("% diabetes")
    plt.ylabel("Wages")
    plt.grid()
    plt.savefig("wages_diabetes.png")
    plt.show()   
    #plotly_graphs(health_income)


if __name__ == "__main__":
    main()















