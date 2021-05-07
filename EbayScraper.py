from requests import get
from bs4 import BeautifulSoup
import pandas as pd

class Ebay:
    data = pd.DataFrame()
    writer = pd.ExcelWriter('CarData_ebay.xlsx')

    def __init__(self, url, car):
        response = get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        posts = soup.find_all('div', {'class': 's-item__info clearfix'})

        for post in posts:
            try:
                try:
                    title = post.find('h3', {'class': 's-item__title'}).find('span', {'class': 'BOLD'}).text.strip()
                except:
                    title = post.find('h3', {'class': 's-item__title'}).text.strip()
                # if car.lower() not in title.lower():
                #     continue
                try:
                    price = post.find('span', {'class': 's-item__price'}).find('span', {'class': 'POSITIVE'}).text.strip()
                except:
                    price = post.find('span', {'class': 's-item__price'}).text.strip()
                post_url = post.find('a', {'class': 's-item__link'})['href']
                post_response = get(post_url)
                post_soup = BeautifulSoup(post_response.text, 'html.parser')
                info1 = post_soup.find_all('td', {'class': 'attrLabels'})
                info2 = post_soup.find_all('td', {'width': '50.0%'})
                details = dict()
                for i, key in enumerate(info1):
                    details[key.text.strip()] = info2[i].text.strip()
                details['url'], details['price'] = post_url, price

                df = pd.DataFrame()
                df = df.append(details, ignore_index=True)
                self.data = self.data.append(df)
                print(title + " completed")

            except:
                pass

        self.data.to_excel(self.writer, car)
        self.writer.save()

url = [
    'https://www.ebay.com/sch/Cars-Trucks/6001/i.html?makeval=Ford&modelval=Mustang&_nkw=Ford+Mustang&_blrs=recall_filtering&Transmission=Manual&LH_All=1&UF_single_selection=Make%3AFord%2CModel%3AMustang&UF_context=finderType%3AVEHICLE_FINDER&_sacat=6001&_stpos=67220&_fspt=1&Model%2520Year=1980%7C1981%7C1982%7C1983%7C1984%7C1985%7C1986%7C1987%7C1988%7C1989%7C1990%7C1991%7C1992%7C1993%7C1994%7C1995%7C1996%7C1997%7C1998%7C1999%7C2000%7C2001%7C2002%7C2003%7C2004%7C2005%7C2006%7C2007%7C2008%7C2009%7C2010%7C2011%7C2012%7C2013%7C2014%7C2015%7C2016%7C2017%7C2018%7C2019%7C2020%7C2021&Number%2520of%2520Cylinders=6%7C8&_fsrp=1&_sop=2&_ipg=200&_oaa=1&_dcat=6236&rt=nc',
    'https://www.ebay.com/sch/Cars-Trucks/6001/i.html?_from=R40&_sop=2&Transmission=Manual&UF_single_selection=Make%3ANissan%2CModel%3A350Z&UF_context=finderType%3AVEHICLE_FINDER&_sacat=6001&_stpos=67220&_fspt=1&Model%2520Year=1980%7C1981%7C1982%7C1983%7C1984%7C1985%7C1986%7C1987%7C1988%7C1989%7C1990%7C1991%7C1992%7C1993%7C1994%7C1995%7C1996%7C1997%7C1998%7C1999%7C2000%7C2001%7C2002%7C2003%7C2004%7C2005%7C2006%7C2007%7C2008%7C2009%7C2010%7C2011%7C2012%7C2013%7C2014%7C2015%7C2016%7C2017%7C2018%7C2019%7C2020%7C2021&_nkw=Nissan+350Z&rt=nc&_oaa=1&_dcat=31864',
    'https://www.ebay.com/sch/Cars-Trucks/6001/i.html?_from=R40&LH_TitleDesc=0&_sop=2&Transmission=Manual&_dcat=84160&UF_single_selection=Make%3ASubaru%2CModel%3AWRX&UF_context=finderType%3AVEHICLE_FINDER&_sacat=6001&_stpos=67220&_fspt=1&Model%2520Year=1980%7C1981%7C1982%7C1983%7C1984%7C1985%7C1986%7C1987%7C1988%7C1989%7C1990%7C1991%7C1992%7C1993%7C1994%7C1995%7C1996%7C1997%7C1998%7C1999%7C2000%7C2001%7C2002%7C2003%7C2004%7C2005%7C2006%7C2007%7C2008%7C2009%7C2010%7C2011%7C2012%7C2013%7C2014%7C2015%7C2016%7C2017%7C2018%7C2019%7C2020%7C2021&_nkw=Subaru+WRX&rt=nc&_blrs=recall_filtering',
    'https://www.ebay.com/sch/Cars-Trucks/6001/i.html?_dcat=6324&makeval=Mazda&_sop=2&Transmission=Manual&_fsrp=1&modelval=Miata&_nkw=Mazda+Miata&UF_single_selection=Make%3AMazda%2CModel%3AMiata&UF_context=finderType%3AVEHICLE_FINDER&_sacat=6001&_stpos=67220&_fspt=1&Model%2520Year=1980%7C1981%7C1982%7C1983%7C1984%7C1985%7C1986%7C1987%7C1988%7C1989%7C1990%7C1991%7C1992%7C1993%7C1994%7C1995%7C1996%7C1997%7C1998%7C1999%7C2000%7C2001%7C2002%7C2003%7C2004%7C2005%7C2006%7C2007%7C2008%7C2009%7C2010%7C2011%7C2012%7C2013%7C2014%7C2015%7C2016%7C2017%7C2018%7C2019%7C2020%7C2021&rt=nc'
]
car = [
    'Mustang',
    '350z',
    'WRX',
    'Miata',
]
# Ebay(url, car)
for u in range(0, len(url)):
    Ebay(url[u], car[u])


