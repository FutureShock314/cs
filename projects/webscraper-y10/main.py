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
