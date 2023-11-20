import json, random

with open('./help.json', 'r') as f:
    helpJson = json.load(f)['commands']

# TODO: use a list to randomly print a different entry to the cmd prompt
# TODO: use a bash script/shell file (.sh) to run clear, use (bash './{ filename }')

print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
print('Some Guy\'s Random Command Prompt\nAll Right Reserved\nThis is mine :D\n\n')
command = input(f'Type a command and press <Enter>, or type \'help\' for more info.\nUser@SomeMachine{random.randint(100, 999)}$ ')
