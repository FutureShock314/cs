import firebase_admin, json, os
from firebase_admin import db
from rich.prompt import Confirm
# if run from main.py, will import from auth.{module}, otherwise pull from this dir
try:
    from auth.exists import exists
    from auth.create import createUser
    from auth.database import Database
except:
    from exists import exists
    from create import createUser
    from database import Database

def auth():

    # db = Database(cred_path = './auth/cs-webscraper.json', ref = '/auth/')
    # db.addUser({'a': 'b', 'c': 'd'})
    # db.addUserJson({'a': 'b'}, 'users.json')
    # db.readUsers()
    # db.readUsersJson('users.json')

    filePath = 'users.json'
    ref = ''

    if db.usingFirebase:
        usingFirebase = True
    else:
        print('Failed to connect to Firebase!')
        print('Fallback to JSON system.')
        print('You may need to recreate your account if you have not previously in this state.')
        if not os.path.exists(filePath):
            with open(filePath, 'w'):
                ...
        with open(filePath, 'r') as f:
            users = json.load(f)
        usingFirebase = False

    exist = Confirm.ask('Have you created an account here before?')

    if exist:
        if exists(users):
            return True
    else:
        create = Confirm.ask('create one?')
        if create:
            if createUser(users, usingFirebase, ref, filePath):
                return True
        else:
            print('in which case, bye bye')
            quit()



if __name__ == '__main__':
    # auth()
    from database import Database
    db = Database(cred_path = './cs-webscraper.json', ref = '/auth/')
    db.addUser({'a': 'b', 'c': 'd'})