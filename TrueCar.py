import pandas as pd
from bs4 import BeautifulSoup
from requests import get
from time import sleep

class TrueCar:
    # try:
        # writer = pd.ExcelWriter('CarData.xlsx', mode='a')
    # except FileNotFoundError:
    writer = pd.ExcelWriter('CarData.xlsx', mode='a')

    data = pd.DataFrame()
    info = [
        'Exterior Color',
        'Style',
        'Interior Color',
        'MPG',
        'Engine',
        'Transmission',
        'Drive Type',
        'Fuel Type',
        'Mileage',
        'Options'
    ]
    year = range(0, 99)
    years = range(1980, 2021)
    def __init__(self, url, car):
        r = get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        pages = soup.find_all('a', {'class': 'page-link'})[-3]['aria-label'].split(" ")[1]
        pages = int(pages)
        if pages > 30:
            pages = 30
        for i in range(1, pages):
            temp_url = url + "&page="+ str(i)
            r = get(temp_url)
            soup = BeautifulSoup(r.text, 'html.parser')
            posts = soup.find_all('a', {'class': 'linkable order-2 vehicle-card-overlay'})
            prices = soup.find_all('div',{'class':'heading-3 margin-y-1 font-weight-bold'})
            # try:
            for index, p in enumerate(posts):
                try:
                    new_url = "https://truecar.com" + p['href']
                    new_r = get(new_url)
                    new_soup = BeautifulSoup(new_r.text, 'html.parser')
                    title = new_soup.find('title').text
                    temp = title.split(" ")
                    for j in temp:
                        try:
                            if int(j) in years or int(j) in year:
                                yrs = j
                        except:
                            pass

                    price = prices[index].text
                    unsplit_info = new_soup.find_all('div', {'class': 'padding-left-1'})
                    split_info = dict()
                    for i in range(0, len(unsplit_info)):
                        inf = unsplit_info[i].text.split(self.info[i])
                        split_info[self.info[i]] = inf[1]
                    split_info['url'], split_info['price'] = new_url, price
                    split_info['year'] = yrs
                    
                    df = pd.DataFrame()
                    df = df.append(split_info, ignore_index=True)
                    self.data = self.data.append(df)
                    print(title + " completed")
                    # sleep(1)
                except:
                    pass
            # except:
            #     pass

        self.data.to_excel(self.writer, car)
        self.writer.save()

url = [
    'https://www.truecar.com/used-cars-for-sale/listings/ford/mustang/location-wichita-ks/?engine[]=6%20Cylinder&engine[]=8%20Cylinder&searchRadius=5000&sort[]=price_asc&titleHistory[]=hide-lemon&titleHistory[]=hide-frame-damage&titleHistory[]=hide-theft-recovery&titleHistory[]=hide-salvage&transmission[]=Manual',
    'https://www.truecar.com/used-cars-for-sale/listings/nissan/350z/location-wichita-ks/?searchRadius=5000&sort[]=price_asc&titleHistory[]=hide-lemon&titleHistory[]=hide-frame-damage&titleHistory[]=hide-theft-recovery&titleHistory[]=hide-salvage&transmission[]=Manual',
    'https://www.truecar.com/used-cars-for-sale/listings/subaru/wrx/location-wichita-ks/?searchRadius=5000&sort[]=price_asc&titleHistory[]=hide-lemon&titleHistory[]=hide-frame-damage&titleHistory[]=hide-theft-recovery&titleHistory[]=hide-salvage&transmission[]=Manual',
    'https://www.truecar.com/used-cars-for-sale/listings/mazda/mx-5-miata/location-wichita-ks/?searchRadius=5000&sort[]=price_asc&titleHistory[]=hide-lemon&titleHistory[]=hide-frame-damage&titleHistory[]=hide-theft-recovery&titleHistory[]=hide-salvage&transmission[]=Manual'
]

car = [
    'Mustang',
    '350z',
    'WRX',
    'Miata'
]

for i in range(0, 4):
    TrueCar(url[i], car[i])
