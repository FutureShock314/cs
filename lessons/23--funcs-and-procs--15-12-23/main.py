import random

a, b = 0, 0

def compare(a: int, b: int):
    if a > b:
        print(a, '( the first person/roll won )')
    elif b > a:
        print(b, '( the second person/roll won )')
    elif a == b:
        print('theyre the same lol')

def getDiceRoll():
    return random.randint(1, 6)

again = ''

while again.lower() != 'no':
    d1, d2 = getDiceRoll(), getDiceRoll()
    compare(d1, d2)
    again = input('again? (Y/n)')
    print(a)
