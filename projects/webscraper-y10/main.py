import requests, pandas as pd
from bs4 import BeautifulSoup

url = 'https://www.metoffice.gov.uk/weather/forecast/gcnhtfzhd#'
r = requests.get(url)

# print(r.content)

soup = BeautifulSoup(r.content, 'html.parser')
day = soup.find('div', attrs = {'aria-labelledby': 'day0Header'})
# print(day)
items_time = soup.find_all('th', id = lambda x: x and x.startswith('d0t'))
times = [item.get_text().strip() for item in items_time]
print(times)

items_temp = soup.find_all('td', attrs = {'headers': lambda x: x and x.startswith('d0Temp d0t')})
# temps = [BeautifulSoup(item, 'html.parser').find_all('div') for item in items_temp]
temp0 = items_temp[0]
temps = BeautifulSoup(temp0, 'html.parser').find('div')
print(temps)
