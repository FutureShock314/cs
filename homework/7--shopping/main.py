import json, random, os

with open('./help.json', 'r') as f:
    helpJson = json.load(f)['commands']

# TODO: use a list to randomly print a different entry to the cmd prompt

def cmdHelp(cmd: list):
    if len(cmd) == 1:
        for cmdName in helpJson.keys():
            print(f'{cmdName}:\n\tsyntax:\t  {helpJson[cmdName]["syntax"]}\n\tdesc:\t  {helpJson[cmdName]["desc"]}\n')

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
    command = input(f'User@SomeMachine{computerNum}$ ')
    if command == 'exit':
        os.system('clear')
        quit()

    if command == 'help':
        cmdHelp(command.split(' '))
