import firebase_admin, json, os
# from firebase_admin import db
from rich.prompt import Confirm
# if run from main.py, will import from auth.{module}, otherwise pull from this dir
if __name__ != '__main__':
    from auth.exists import exists
    from auth.create import createUser
    from auth.database import Db as db
else:
    from exists import exists
    from create import createUser
    from database import Db as db

def auth():

    # db.addUser({'a': 'b', 'c': 'd'})
    # db.addUserJson({'a': 'b'}, 'users.json')
    # db.readUsers()
    # db.readUsersJson('users.json')

    # print(db.usingFirebase)

    if db.usingFirebase:
        users = db.getUsers()
    else:
        print('Failed to connect to Firebase!')
        print('Fallback to JSON system.')
        print('You may need to recreate your account if you have not previously in this state.')
        users = db.getUsersJson()

    exist = Confirm.ask('Have you created an account here before?')

    if exist:
        if exists(users):
            return True
    else:
        create = Confirm.ask('create one?')
        if create:
            if createUser(users):
                return True
        else:
            print('in which case, bye bye')
            quit()



if __name__ == '__main__':
    # auth()
    from database import Database
    db = Database(cred_path = './cs-webscraper.json', ref = '/auth/')
    db.addUser({'a': 'b', 'c': 'd'})