import pandas as pd
from bs4 import BeautifulSoup
from requests import get

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}
print(headers)
url = 'https://www.cargurus.com/Cars/inventorylisting/viewDetailsFilterViewInventoryListing.action?sourceContext=carGurusHomePageModel&entitySelectingHelper.selectedEntity=d2&zip=67220'
print(url)

response = get(url, headers=headers)
print(response)

soup = BeautifulSoup(response.text, 'html.parser')
posts = soup.find_all('a', {'data-cg-ft': 'car-blade-link', 'class': '_4Pn4Gb _2yn1Hf'})
print(soup)