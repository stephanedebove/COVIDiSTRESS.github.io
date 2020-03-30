# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 14:27:28 2020

@author: Paula
"""

import pandas as pd
import codecs

data = pd.read_csv("contributors.csv", header=1)
data = data.iloc[:, :2]

with codecs.open("contributors_table.md", "w", "utf-8") as f:
    print("| *Name* 	| *Institution*	|", file=f)
    print("|:-----------------------------------	|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|",file=f)
    for row in data.iterrows():
        name, inst = row[1]
        if type(inst) is not str:
            inst = "Independent Researcher"
        print("|" + name +	"|" + inst +"|", file=f)
    f.flush()