'''tasks ig'''

from random import randint
import time # for task 2

num = randint(1, 10)
guess = 0
while guess != num:
    guess = int(input('guess\n>> '))
    if guess == num:
        print('youre not bad')
    else:
        print('bad lol')


# Task 2

while True:
    comp = randint(1, 6)
    usr = randint(1, 6)
    print(f'computer rolled { comp }')
    time.sleep(randint(1, 10))
    print(f'user rolled { usr }')
    if usr > comp:
        print('usr wins')
    else:
        print('usr bad')
