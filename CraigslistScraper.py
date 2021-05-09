from requests import get
from bs4 import BeautifulSoup
import pandas as pd

class Craigslist:
    years = range(1980,2021)
    years2 = range(0, 100)
    data = pd.DataFrame()
    writer = pd.ExcelWriter('CarData_craigslist.xlsx', mode='wa')

    def __init__(self, url, car):
        response = get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        posts = soup.find_all('li', class_='result-row')

        for post in posts:
            title = post.h3.text.strip()
            # if car.lower() not in title.lower():
            #     continue
            temp = title.split(" ")
            index = 0
            # Grab the year
            while index < len(temp):
                try:
                    year = int(temp[index])
                    if year in self.years or year in self.years2:
                        break
                except ValueError:
                    index +=1
            
            # Grab other info
            price = post.find('span', {'class': 'result-price'}).text.strip()
            post_url = post.find('a', class_='result-title hdrlnk')['href']
            post_response = get(post_url)
            post_soup = BeautifulSoup(post_response.text, 'html.parser')
            info = post_soup.find_all('p', class_='attrgroup')[1].find_all('span')
            details = dict()
            for i in info:
                split = i.text.strip().split(": ")
                try:
                    details[split[0]] = split[1]
                except IndexError:
                    split = i.text.strip().split(" ")
                    details[split[0]] = split[1]

            details['year'], details['url'], details['price'] = year, post_url, price

            df = pd.DataFrame()
            df = df.append(details, ignore_index=True)

            self.data = self.data.append(df)
            print(title + " completed")

        self.data.to_excel(self.writer, car)
        self.writer.save()


url = [
    r'https://wichita.craigslist.org/search/cta?sort=priceasc&purveyor-input=all&hasPic=1&bundleDuplicates=1&search_distance=10000&postal=67220&min_price=500&auto_make_model=ford+mustang&min_auto_year=1980&auto_cylinders=4&auto_cylinders=5&auto_transmission=1',
    r'https://wichita.craigslist.org/search/cta?query=nissan+350z&sort=priceasc&purveyor-input=all&hasPic=1&bundleDuplicates=1&search_distance=10000&postal=67220&min_price=500&auto_make_model=nissan+350z&auto_transmission=1',
    r'https://wichita.craigslist.org/search/cta?query=subaru+wrx&sort=priceasc&purveyor-input=all&hasPic=1&bundleDuplicates=1&search_distance=10000&postal=67220&min_price=500&auto_make_model=subaru+wrx&auto_transmission=1',
    r'https://wichita.craigslist.org/search/cta?sort=priceasc&purveyor-input=all&hasPic=1&bundleDuplicates=1&search_distance=10000&postal=67220&auto_make_model=mazda+miata&auto_transmission=1'
]
car = [
    'Mustang',
    '350z',
    'WRX',
    'Miata'
]
# Craigslist(url[2], car[2])
for u in range(0, len(url)):
    Craigslist(url[u], car[u])


# mustang = Craigslist(url[0], car[0])
# print(mustang.data)
