from time import sleep
# import math

print('\nGood day, old chap!')
sleep(1)

print('My name\'s Sir Charles, Duke of Essex, and thou shalt address me as such, peasant')
sleep(3)

name = input('Now that the important pleasantries are over, \
it would be rude of me to not ask your name?\n>> ')
sleep(1)

print(f'Sorry, did you say {name}?')
sleep(.5)
print('Yes??')
sleep(.5)
print('Haha, forgive me, but that name is utterly hilarious!')
sleep(0.2)
print('How can you possibly live with such a ridiculous name?')
for i in range(5):
    sleep(i)
    print('Ha')

sleep(3)
print('Well, that was awkward')
sleep(0.5)
print('Anyways, now that that\'s over, it would also be rude of me to not ask how you are?')
input('>> ')

print('yes, yes, good and all that jazz, I\'m feeling rather splendid today, thanks for asking')
sleep(3)
print('so, onto the important stuff.')
sleep(2)
print('The Stock Market')
sleep(4)
follows = input('Do you follow the stock market, peasant?\n>> ')
if follows.upper() == 'YES' or follows.upper() == 'Y':
    print('well, I don\'t, so have a good day, chap')
elif follows.upper() == 'NO' or follows.upper() == 'N':
    print('neither lol')
else:
    print('you little bugger')
    sleep(1)
    print('get away from me right bloody now')
