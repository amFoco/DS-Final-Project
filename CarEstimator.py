"""
CarEstimator: This program is to estimate the price of cars by way of machine learning.
The data for this will be scraped off of the following websites:
    - Craigslist
    - Ebay
    - Facebook Marketplace
    - Offerup (maybe)
The data will be collected off of the following cars:
    - Ford Mustang
    - Nissan 350z
    - Mazda Miata
    - Subaru WRX
The cars will be picked based on:
    - # of cylinders
    - Transmission type
    - title
    - condition
"""

import numpy as np
import pandas as pd
import sqlite3 as sq
from bs4 import BeautifulSoup

data = {
    'Mustang':pd.DataFrame(),
    '350z': pd.DataFrame(),
    'WRX': pd.DataFrame(),
    'Miata': pd.DataFrame()
}

truecar = pd.read_excel(r'C:\Users\asix.NIAR\Desktop\Homework\DataScience\FinalProject\DS-Final-Project\CarData.xlsx', sheet_name=None)
ebay = pd.read_excel(r'C:\Users\asix.NIAR\Desktop\Homework\DataScience\FinalProject\DS-Final-Project\CarData_evay.xlsx', sheet_name=None)
craigslist = pd.read_excel(r'C:\Users\asix.NIAR\Desktop\Homework\DataScience\FinalProject\DS-Final-Project\CarData_craigslist.xlsx', sheet_name=None)

for i in truecar.keys():
    truecar[i] = truecar[i][truecar[i]['Engine'].dropna()]
    data[i].append(truecar[i])
for i in ebay in ebay.keys():
    ebay[i] = ebay[i][truecar[i]['Engine'].dropna()]
    data[i].append(ebay[i])
for i in craigslist.keys():
    craigslist[i] = craigslist[i][craigslist[i]['Engine'].dropna()]
    data[i].append(craigslist[i])