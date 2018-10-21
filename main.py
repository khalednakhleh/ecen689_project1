#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 16:40:47 2018

Name: khalednakhleh
"""


import pandas as pd
import numpy as np



health = pd.read_csv("health_data.csv")

income = pd.read_csv("good_income_data.csv")

print(health.shape)
print(income.shape)