import requests, pandas as pd
from bs4 import BeautifulSoup

url = 'https://www.metoffice.gov.uk/weather/forecast/gcnhtfzhd#'
r = requests.get(url)
