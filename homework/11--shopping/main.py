from time import sleep as sl

items = {
    'tshirt': 10,
    'a singular apple (hat)': 1_000,
    'ive run out of ideas already': 27.26581749507193,
    'why am i doing this': 2_147_483_647,
    'generic item people buy': 2,
    'a shirt': 35,
    'something purple idk': 46,
    'a blouse or something': 72.5,
    'a cap': 300,
    'a tie': 6750
}

sl(1)

print('howdy')
print('so do you like')
sl(1)
print('want to buy something')

doTheyWantToBuyAnythingBecauseLongVarNameGoBrrrrrrrrrrrrrrrrrrrr = input('y/n')

if doTheyWantToBuyAnythingBecauseLongVarNameGoBrrrrrrrrrrrrrrrrrrrr.lower() != 'y':
    print('ok')
    quit()

stop = ''
cost = 0
bought = []

while stop.lower() != 'y':
    print(items)
    wants = input('so whaddaya want\n')
    if wants in items.keys():
        cost += items[wants]
        bought.append(wants)
    else:
        print('doesnt exist lol')
    stop = input('do you want to stop\n(y/n)>> ')
    if stop != 'y':
        print('on we go then')

print('aww whyd you stop')
print('boring')
print('anyway heres your bill')
print(cost)
print(f'from {bought}')

if 'why am i doing this' in bought:
    print('you rich moron')
    print('you spent the 32bit integer limit')
    print('stupid')
    print('yk what you dont get to pay')
    quit()

doTheyWantToPayOrNotBecauseLongerVariableNameGoBrrrrrrrrrrrrrrrrrrrrrrrrrrr = input('pay?\n(y/n)>> ')

if doTheyWantToPayOrNotBecauseLongerVariableNameGoBrrrrrrrrrrrrrrrrrrrrrrrrrrr != 'y':
    print('have fun with your stolen goods')
else:
    print('thanks lol')
    print(f'your new bank balance is -{cost}')
