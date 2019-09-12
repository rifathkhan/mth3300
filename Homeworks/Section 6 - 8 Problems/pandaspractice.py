# -*- coding: utf-8 -*-
"""
Created on Thu May 16 13:40:28 2019

@author: khanr
"""

import pandas as pd

x = pd.read_csv("sales.csv")

print(x[['customer','sale']])

person = "Albert"

x.loc[x['customer'] == person]


