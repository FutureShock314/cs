import json, random, os

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
    try:
        list.append(cmd[1])
        print(f'Successfully added {cmd[1]} to the list!\n')
    except:
        print(f'Failed to add {cmd[1]} to the list. Not sure how you did this\n')

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
        for i in range(len(shoppingList)):
            print(f'{i + 1}. {shoppingList[i]}')
        print()
