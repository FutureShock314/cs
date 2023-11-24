from rich.prompt import Confirm
import getpass, json

def auth():
    makeNew = Confirm.ask('create a new user?')
    if makeNew:
        username = input('Please create a username\n>> ')
        while username == '':
            username = input('Please create a username\n>> ')

        password = getpass.getpass(prompt='Please create a password (you won\'t see as its inputted)\n>> ', stream=None)
        print(password)
    else:
        loop = True
        while loop == True:
            username = input('Please enter your username\n>> ')
            with open('./users.json', 'r') as f:
                f = json.load(f)
                if username in f.keys():
                    loop = False
                    password = getpass.getpass(prompt='Please enter your password (you won\'t see as its inputted)\n>> ', stream=None)
                    if password == f[username]:
                        authenticated = True
                        return authenticated
                    else:
                        print('Incorrect password')
                else:
                    print(f'User {username} does not exist.')
