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

if __name__ == '__main__':
    fetchNews()
