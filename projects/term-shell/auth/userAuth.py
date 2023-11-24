from rich.prompt import Confirm
import getpass, json

def auth():
    with open('./users.json', 'r') as f:
        users = json.load(f)
    while True:
        makeNew = Confirm.ask('create a new user?')
        if makeNew:
            username = input('Please create a username\n>> ')
            while username == '':
                username = input('Please create a username\n>> ')

            password = getpass.getpass(prompt='Please create a password (you won\'t see as its inputted)\n>> ', stream=None)

            with open('./users.json', 'w') as f:
                try:
                    users[username] = password
                    users = json.dumps(users)
                    f.write(users)
                except:
                    print('Failed to add user.')
                    continue

        else:
            while Confirm.ask('Change username inputted?') == True:
                username = input('Please enter your username\n>> ')
                while username not in users.keys():
                    print(f'User {username} does not exist.')
                    continue

                password = getpass.getpass(prompt='Please enter your password (you won\'t see as its inputted)\n>> ', stream=None)
                if password == f[username]:
                    break
                else:
                    print('Incorrect password')
