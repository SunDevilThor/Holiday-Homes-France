# Holiday Homes - UK
# Tutorial from John Watson Rooney YouTube channel

import requests 
from bs4 import BeautifulSoup
import time
import pandas as pd

holiday_homes = []

for page in range(1, 30):

    url = f'https://www.holidayfrancedirect.co.uk/cottages-holidays/index.htm?board=sc&d=France&people=2&prop_type[0]=cottagegite&page='

    response = requests.get(url + str(page)) 

    soup = BeautifulSoup(response.content, 'html.parser')

    content = soup.find_all('div', class_= 'property-grid-item')


    for property in content: 
        title = property.find('h2').text
        bedrooms = property.find('p', class_= 'property-spec').text
        price = property.find('div', class_= 'property-pricing').text

        # Puts items into a dictionary
        property_info = {
            'title': title, 
            'bedrooms': bedrooms, 
            'price': price
        }

        # Puts all the dictionaries into one main list
        holiday_homes.append(property_info)
        print('Holiday Homes Found: ', len(holiday_homes))
        #time.sleep(2)

df = pd.DataFrame(holiday_homes)
print(df.head())
df.to_csv('Holiday-Homes-UK.csv')
print('Sent items to CSV file')