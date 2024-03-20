from random import randint

class SkillIssue(Exception):
    def __init__(self, message='lol bad'):
        self.message = message
        super().__init__(self.message)

auth1 = input('Auth 1:\nInput UserID: ')
users = ['Talin', 'Ayaan', 'Jake']

if not users[int(auth1)]:
    print('you little brat trying to get into my system you stupid nerd')
    quit()

auth2 = input('Auth 2: ')

if auth2 != '314159265':
    print('you little brat trying to get into my system you stupid nerd')
    quit()
    
# auth3

num1 = input('Auth 3:\n Input number: ')
num2 = input('Input number: ')

if int(num1) * int(num2) != 420:
    print('you little brat trying to get into my system you stupid nerd')
    quit()
    
try:
    with open('prevlaunch.txt', 'r') as f:
        print('Previous launch: ')
        print(f.read())
except:
    print('No previous launch data')

loc = input('Select destination: ')
missiles = ['A2A', 'Ballistic', 'ICBM']

for i in range(len(missiles)):
    print(f'{i}: {missiles[i]}')

missile = input('Pick a missile: ')

if not int(missile):
    print('no')
    quit()

if not int(missile) < 4:
    print('no')
    quit()

fail = randint(1, 100)

print(f'Chance of failure: {fail}%')

cont = input('Do you wish to continue? [Y/n]: ')

if cont not in ['y', 'Y', '', None]:
    print('okie dokie')
    quit()

if randint(1, 100) < fail:
    print('lol missile exploded in your face you die bozo')
    raise SkillIssue('L')

for i in range(10):
    print(10 - i)
    time.sleep(1)

print(f'Missile landed at {loc}')
casualties = (100 - fail) * 423650
print(f'Casualties: {casualties}')

with open('prevlaunch.txt', 'w') as f:
    f.write(f'authorised by ID: {users[int(auth1)]}\nLocation: {loc}\nCasualties: {casualties}')

print('ok bye bye now')

