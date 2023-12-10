import json, getpass
from rich.prompt import Confirm
from auth.passAuth import passAuth
from auth.root import root

def makeUser():
    with open('./users.json', 'r') as f:
        existingUsers = json.load(f)

    # predefine username and password
    username, password, tryAgain = '', '', True

    make = Confirm.ask('Would you like to create an account?')

    if make:
        while tryAgain:
            while username == '' or username in existingUsers.keys():
                username = input('Please enter a username\n>> ')
                if username == '':
                    print('Cannot have a blank username.')
                elif username in existingUsers.keys():
                    if username == 'root':
                        if root():
                            return True, 'root'
                    else:
                        print(f'User \'{username}\' already exists.')
                        logIn = Confirm.ask('Would you like to log in to this username?')
                        if logIn:
                            if passAuth(username):
                                return True, username

            while len(password) < 3:
                password = getpass.getpass('Please enter a password, you won\'t see it as you input it\n>> ')
                if len(password) < 3:
                    print('Password too short.')
                elif password == '':
                    print('Cannot have a blank password.')
            
            try:
                existingUsers[username] = password
                existingUsers = json.dumps(existingUsers, indent=4)
                with open('./users.json', 'w') as f:
                    f.write(existingUsers)
                print('Successfully added account!')
                return True, username
            except:
                print('Failed to add account.')
                tryAgain = Confirm.ask('Try again?')
                if tryAgain:
                    continue
                else:
                    print('Exiting...')
                    return False
                    quit()
    else:
        print('Exiting...')
        quit()
