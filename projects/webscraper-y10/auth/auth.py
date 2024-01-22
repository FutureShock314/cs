import firebase_admin, json, os
from firebase_admin import db
from rich.prompt import Confirm
# if run from main.py, will import from auth.exists, otherwise pull from this dir
try:
    from auth.exists import exists
    from auth.create import createUser
except:
    from exists import exists
    from create import createUser

def auth():

    filePath = 'users.json'
    ref = ''

    try:
        cred_object = firebase_admin.credentials.Certificate('./auth/cs-webscraper.json')
        default_app = firebase_admin.initialize_app(cred_object, {
            'databaseURL': 'https://cs-webscraper-y10-default-rtdb.europe-west1.firebasedatabase.app/'
        })
        ref = db.reference('/auth')
        users = ref.get()
        usingFirebase = True
    except:
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
    auth()