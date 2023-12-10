import random
from time import sleep

times_table = 5
for x in range(1, 11):
    print(times_table * x)
    for x in range(random.randint(1, 10)):
        print(x)

sleep(1)
print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

x = 1
for i in range(300):
    x *= 10 * i
    print(x)

for i in range(1, 11):
    print(i * 12)
