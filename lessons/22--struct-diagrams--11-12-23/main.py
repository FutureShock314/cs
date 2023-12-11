import random

flip = random.randint(1, 2)

choice = input('pick 1 (h) or 2 (t)\n>> ')

while choice != '1' and choice != '2':
    print('mate i want a 1 or 2')
    choice = input('pick 1 (h) or 2 (t)\n>> ')

choice = int(choice)

if choice == flip:
    print('yay you win so cool yippee /s')
else:
    print('bad lol')


# >============< something >============<