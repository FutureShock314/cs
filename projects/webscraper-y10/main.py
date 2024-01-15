import requests, pandas as pd
from bs4 import BeautifulSoup

url = 'https://www.metoffice.gov.uk/weather/forecast/gcnhtfzhd#'
r = requests.get(url)

# print(r.content)

soup = BeautifulSoup(r.content, 'html.parser')
day = soup.find('div', attrs = {'aria-labelledby': 'day0Header'})
print(day)
