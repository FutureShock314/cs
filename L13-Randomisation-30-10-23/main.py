# import random
import random

# set num to random val
num = random.randrange(1, 101)

# take an input as 'guess'
guess = input('give num')

# compare guess and num
if int(guess) == num:
    print('ya got it righ')
else:
    print('L')

# Q2
# import randrange function from random
from random import randrange

# set word to val
word = 'STUBrislington'

# set 3 random nums from 1 to 99
num1 = randrange(1, 100)
num2 = randrange(1, 100)
num3 = randrange(1, 100)

# add the 3 nums to the word to form a password
password = word + str(num1) + str(num2) + str(num3)


