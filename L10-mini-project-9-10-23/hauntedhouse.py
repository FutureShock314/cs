from time import sleep

def pr(a:str):
    print(a)

def sl(a):
    sleep(a)

for i in range(5):
    sleep(i)
    print('\n')

print('you wake up')
sleep(1)
print('idk what to say here imagine i say something ominous')
sleep(1)
print('as your vision clears, you see three hallways extending in front of you')
sleep(.5)
print('the left one has a ghost visible')
sleep(.5)
print('the forward one appears clear')
sleep(.5)
print('the right one appears to have a very deep hole (dont you dare)')

sleep(2)

hallway1 = input('which would you like to take? (forward, left, right)')

if 'forward' in hallway1.lower():
    print('yippee im so overjoyed you survived you depressed child')
elif 'left' in hallway1.lower():
    print('ok')
    sleep(1)
    print('you die lol')
    while True:
        print('you have to deal with this now for your eternal haunting')
elif 'right' in hallway1.lower():
    print('bro why')
    sleep(1)
    print('you actual idiot')
    sleep(1)
    print('you die lol')
    while True:
        print('you have to deal with this while you fall endlessly to your death now lol')
else:
    print('bro')
    sleep(1)
    print('no')
    while True:
        print('the ghost comes for you and kills you')

pr('ok so you lived')
sl(1)
pr('well done')
sl(1)
pr('so do you want to go on')
goOn = input()

if goOn.lower() == 'y':
    pr('ok')
else:
    while True:
        pr('deal with it')

pr('ok so you want to go on')
sl(1)
pr('you see a ladder')
sl(1)
pr('you wanna go up or down (up, down)')
upDown = input()

if 'up' in upDown.lower():
    pr('well done')
elif 'down' in upDown.lower():
    pr('L you die with no hints as to which it was a 50/50 but not really')
    while True:
        pr('L')
else:
    while True:
        pr('L')

pr('ok so you got up the ladder right')
sl(1)
pr('and you see')
for i in range(5):
    pr('...')
    sl(1)
pr('a door')
sl(1)
pr('i know right its so cool')
sl(1)
pr('so do you want to go through or look backwards')
through = input()
if 'through' in through:
    pr('okie dokie')
    pr('you win ig')
