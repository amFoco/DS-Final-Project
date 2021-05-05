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

# 6/8 cyls, 

craigslist_urls[
    'https://wichita.craigslist.org/search/sss?query=ford+mustang&sort=priceasc&purveyor-input=all&srchType=T&hasPic=1&search_distance=5000&postal=67220&min_price=1000&auto_transmission=1',
    
]