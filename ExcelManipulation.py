# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 01:24:39 2020

@author: M.Dhia
"""

# Importing the libraries

import pandas as pd
import csv


def location():
    location = location = r'C:\Users\M.Dhia\Desktop\Final\DataSet\DataSetCSV.csv'
    return location
  
  
def addLine(location,newMatier):
    with open(location, 'a') as myfile:
        wr = csv.writer(myfile, quotechar=',')
        wr.writerow(newMatier)

def readCSV(location):
    dataset = pd.read_csv(location)
    return dataset

def dropLastLine(dataset,location):
    dataset.drop(dataset.tail(1).index, inplace=True)
    dataset.to_csv(location, index=False)
    
    
    
    