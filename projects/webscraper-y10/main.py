from auth.auth import auth
from time import sleep as sl
import random, time
# from auth.database import Db as db

from weather import fetchWeather
from news import fetchNews

#! UNCOMMENT THIS FOR FINAL
auth()

... # dont need to check for auth(), if it fails it always quits ( i think )

possible = ['n', 'w', 'news', 'weather'] # makes the while loop easier
input_   = input('What would you like to see, news or weather? [w/n/news/weather]\n>> ')

while input_.lower() not in possible:
    print('not an option mate, you can type n, w, news, or weather')
    sl(1)
    input_ = input('What would you like to see, news or weather? [w/n/news/weather]\n>> ')

if input_.lower() in ['n', 'news']:
    if random.randint(1, 4) == 2:
        fetchWeather() # 25% of weather if news
    else:
        fetchNews()
else:
    if random.randint(1, 4) == 4:
        fetchNews() # 25% of news if weather
    else:
        fetchWeather()
