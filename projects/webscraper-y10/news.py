import requests, pandas as pd, time
from bs4 import BeautifulSoup
from rich.prompt import Confirm
from auth.database import Db as db


def timer(func) -> any:
    def wrapper(*args):
        start = time.time()
        func()
        end = time.time()
        print(f'\noperation took {end - start} seconds')

    return wrapper

def fetchNews() -> None:
    start = time.time()

    print('Fetching the news...')
    url = 'https://www.bbc.co.uk/'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    # print(r.content)
    #? get every item with a class containing PromoLink
    items_headlines = soup.find_all('a', attrs={ 'class': lambda x: x and 'PromoLink' in x })
    text_headlines = [item.get_text() for item in items_headlines]
    headlines = [text_headlines[i] for i in range(9)] #? Only get the first 9 headlines, could do it in the for loop but idk i didnt want to
    # print(headlines)

    headlineNum = 0
    for headline in headlines:
        # print(headline)
        if 'Video' in headline:
            headline = '( VIDEO ) ' + headline.split('Video')[0].strip()
        if ('Live.' in headline) or ('FA Cup:' in headline): #or FA CUP: becase fsr when testing this a live wasnt listed live and it was an FA Cup one so
            headline = '( LIVE ) ' + headline.split('Live.')[-1].strip()
            headlines[headlineNum] = f'Live.{headlines[headlineNum]}'
        print(f'\n {headlineNum + 1}: {headline: <85} ( at: https://bbc.co.uk{items_headlines[headlineNum]["href"]} )')
        headlineNum += 1

    end = time.time()
    print(f'\noperation took {end - start} seconds')

    writeData = {}
    for _ in range(len(headlines)):
        writeData[headlines[_]] = f'https://bbc.com{items_headlines[_]["href"]}'

    db.writeDataJson(path = f'./saved-data/news/{time.strftime("%Y-%m-%d")}', data = writeData)

    if Confirm.ask('Would you like specifics on any articles?'):
        articleNum = 'something'
        while (not articleNum.isdigit()) or (int(articleNum) not in [i for i in range(len(headlines))]):
            articleNum = input('please type the number preceding (coming before) the title of the ARTICLE (cannot say LIVE or VIDEO before it) you wish to see, or type \'no\' or \'exit\' to exit.\n>> ')
            if ' ' in articleNum.strip():
                continue
            #? self explanatory
            if articleNum.lower() == 'no' or articleNum.lower() == 'exit':
                print('exiting...')
                quit()
            if int(articleNum) - 1 < len(headlines):
                #? doesnt allow for checking of a video as it just doesnt work
                if ('Live.' in headlines[int(articleNum)]) or ('Video' in headlines[int(articleNum)]):
                    print('CANT BE A VIDEO OR LIVE')
                    # continue # this didnt work so set articleNum to something that doesnt fulfill to force loop
                    articleNum = 'something that doesnt work'
    else: print('ok'); quit()

    #? new url from href extension and parse said url
    url = f'https://bbc.co.uk{items_headlines[int(articleNum)]["href"]}'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    #? find every div with either Byline or RichText in its class name and append them to a list
    items_article = soup.find('article').find_all('div', attrs = { 'class': lambda x: x and (('Byline' in x) or ('RichText' in x))})
    #? get text from every item in list of article paragraphs, if its the second occurance of it because for some reason there are duplicates
    texts_article = [item.get_text() for item in items_article if items_article.index(item) % 2 == 0] # %2 because duplicates i think because site has 2 because accessibility or smth idk
    for i in range(len(texts_article)):
        print(f'\n{texts_article[i]}')
    else:
        print(f'Read probably better at: {url}')

if __name__ == '__main__':
    fetchNews()
