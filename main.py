#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 16:40:47 2018

Name: khalednakhleh

Run the file parsing.py first to obtain the file combined.csv
"""

import pandas as pd
import matplotlib.pyplot as plt


def main():
    
    health_income = pd.read_csv("combined_2013.csv")
    
    print(health_income.shape)
    
    # Grabbing the health data
    diabetes_2008 = health_income.iloc[:, 4]
    diabetes_2013 = health_income.iloc[:, 5]
    obesity_2008 = health_income.iloc[:, 6]
    obesity_2013 = health_income.iloc[:, 7] 
    joint_return = health_income.iloc[:, 22] 
    
 
    # example to help you get started    

    plt.scatter(diabetes_2008, joint_return)
    plt.show()
    

if __name__ == "__main__":
    main()

