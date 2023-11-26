from rich.Prompt import Confirm
from checkUser import checkUser

def auth():
    isUser = Confirm.ask('Have you used this program before, and created an account? ')

    if isUser:
        continue = Confirm.ask('Would you like to log in? ')
        if continue:
            while True:
                username = input('Please enter your username\n>> ')
                if checkUser(username):
                    if passAuth(username):
                        return True
                else:
                    print('Invalid username.')
                    continue
        else:
            print('Exiting...')
            quit()

