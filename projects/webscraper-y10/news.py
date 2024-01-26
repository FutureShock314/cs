import requests, pandas as pd, time
from bs4 import BeautifulSoup

def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f'operation took {end - start} seconds')
    return wrapper

@timer
def fetchNews():
    ...
    url = 'https://www.bbc.co.uk/'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    # print(r.content)
    items_headlines = soup.find_all('p', attrs = { 'class': lambda x: x and 'PromoHeadline' in x })
    text_headlines = [item.get_text() for item in items_headlines]
    headlines = [text_headlines[i] for i in range(9)]
    print(headlines)

    for headline in headlines:
        print(headline)

if __name__ == '__main__':
    fetchNews()
