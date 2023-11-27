from rich.prompt import Confirm
from auth.checkUser import checkUser
from auth.passAuth import passAuth
from auth.makeUser import makeUser

def auth():
    isUser = Confirm.ask('Have you used this program before, and created an account?')

    if isUser:
        willContinue = Confirm.ask('Would you like to log in?')
        if willContinue:
            while True:
                username = input('Please enter your username\n>> ')
                if checkUser(username):
                    if passAuth(username):
                        return True, username
                else:
                    print('Invalid username.')
                    continue
        else:
            print('Exiting...')
            quit()

    # if not already a user, ask if they want to create an account
    else:
        madeUser = makeUser()
        print(madeUser)
        if madeUser[0]:
            return True, madeUser[1]
        else:
            return madeUser[0]
