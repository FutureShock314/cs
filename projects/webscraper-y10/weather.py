import requests, pandas as pd
from bs4 import BeautifulSoup

def fetchWeather():
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
    temps = [item.find('div').get_text() for item in items_temp]
    print(temps)

    items_rain = soup.find_all('td', attrs = {'headers': lambda x: x and x.startswith('d0PoP d0')})
    rains = [item.get_text().strip() for item in items_rain]
    print(rains)

    # Use + for first \n in order to not show the space before text
    print('\n' + soup.find_all('div', id = lambda x: x and x.startswith('tabSummaryText'))[0].get_text().strip(), '\n')

    for i in range(len(times)):
        print(f'{times[i]} : {temps[i]} : {rains[i]}')

if __name__ == '__main__':
    fetchWeather()
