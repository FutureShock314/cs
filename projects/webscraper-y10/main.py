import requests, pandas as pd
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as bs4

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
temps = []

for item in items_temp:
    itemsoup = item
    temp_item = itemsoup.find('div')
    temps.append(temp_item.get_text())

print(temps)

for i in range(len(temps)):
    print(f'{times[i]}: {temps[i]}')
