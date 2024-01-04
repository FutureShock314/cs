import json, getpass
from time import sleep as sl

def root():
    print('So, you think you\'re root?')
    sl(1)
    print('We\'ll see about that.')
    sl(1)
    name = input('What is the full name of the creator of this shell? ( Case Sensitive )\n>> ')
    sl(1)
    if name != 'Ayaan Waqas':
        print('L you lose')
        return False

    print('So you beat one challenge...')
    sl(1)
    print('But can you beat another?')
    sl(1)
    intlim = input('What is the 32 bit unsigned integer limit? ( no cheating )\n>> ')
    while True:
        try:
            intlim = int(intlim)
            break
        except:
            print('not an int')
            intlim = input('What is the 32 bit signed integer limit? ( no cheating )\n>> ')

    sl(1)
    if intlim != 2_147_483_647:
        print('Nope')
        return False
    print('So you beat yet another')
    sl(1)
    print('I have one more for you.')
    sl(.5)
    print('If you can beat it, you shall earn unrestricted access to whatever this mess is')
    sl(.5)
    print('The final challenge is...')
    for i in range(5):
        sl(.5)
        print('.')
    finalChallenge = input('What\'s 9 + 10?\n>> ')
    sl(1)
    if finalChallenge != '21':
        for i in range(10):
            print('.' * (i + 1))

        print('LLLLLLLLLLLLLLLLL')
        return False
    else:
        return True
