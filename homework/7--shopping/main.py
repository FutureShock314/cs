import json, random, os
from rich import print

with open('./help.json', 'r') as f:
    helpJson = json.load(f)['commands']

# TODO: use a list to randomly print a different entry to the cmd prompt

shoppingList = []

def cmdHelp(cmd: list):
    if len(cmd) == 1:
        for cmdName in helpJson.keys():
            print(f'{cmdName}:\n\tsyntax:\t  {helpJson[cmdName]["syntax"]}\n\tdesc:\t  {helpJson[cmdName]["desc"]}\n')
    elif cmd[1] in helpJson.keys():
        print(f'Help for {cmd[1]}:\n\tsyntax:\t  {helpJson[cmd[1]]["syntax"]}\n\tdesc:\t  {helpJson[cmd[1]]["desc"]}\n')
    else:
        print(f'No command \'{cmd[1]}\' found')

def cmdAdd(cmd: list):
    list = shoppingList
    if len(cmd) > 1:
        try:
            print('Successfully added items: ')
            for i in range(1, len(cmd)):
                list.append(cmd[i])
                print(f'\t{i}. {cmd[i]}')
            print('to the list!')
        except:
            print(f'Failed to add items to the list. Not sure how you did this')
    else:
        try:
            list.append(cmd[1])
            print(f'Successfully added {cmd[1]} to the list!')
        except:
            print(f'Failed to add {cmd[1]} to the list. Not sure how you did this')
    print()

def cmdRemove(cmd: list):
    list = shoppingList
    if len(cmd) > 1:
        try:
            for i in range(1, len(cmd)):
                list.remove(cmd[i])
            print('Successfully removed items!')
        except:
            print('Failed to remove items. Perhaps a typo?')
    else:
        try:
            list.remove(cmd[1])
            print(f'Successfully removed {cmd[1]} from the list!')
        except:
            print(f'Failed to remove {cmd[1]}, perhaps a typo?')
    print()

def cmdList(cmd: list):
    list = shoppingList
    if len(cmd) == 1:
        for i in range(len(list)):
            print(f'{i + 1}. {list[i]}')
    elif '--inline' in cmd:
        print(list)
    else:
        print(f'Invalid Parameter(s): {cmd[1:len(cmd)]}')
    print()


os.system('clear')

print('''\
     _                       _
 ___| |__   ___  _ __  _ __ (_)_ __   __ _
/ __| '_ \ / _ \| '_ \| '_ \| | '_ \ / _` |
\__ \ | | | (_) | |_) | |_) | | | | | (_| |
|___/_| |_|\___/| .__/| .__/|_|_| |_|\__, |
                |_|   |_|            |___/
 _ _     _
| (_)___| |_
| | / __| __|
| | \__ \ |_
|_|_|___/\__|
''')

print('Some Guy\'s Random Command Prompt\nAll Right Reserved\nThis is mine :D\n\n')
print('Type a command and press <Enter>, or type \'help\' for more info.')
computerNum = random.randint(100, 999)
command = ''

while command != 'exit':
    command = input(f'User@SomeMachine{computerNum}$ ').split(' ')
    if command[0] == 'exit':
        os.system('clear')
        quit()

    if command[0] == 'help':
        print()
        cmdHelp(command)

    if command[0] == 'add':
        print()
        cmdAdd(command)

    if command[0] == 'list':
        print()
        cmdList(command)

    if command[0] == 'remove':
        print()
        cmdRemove(command)
