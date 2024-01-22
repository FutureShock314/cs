import firebase_admin, json
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

    try:
        cred_object = firebase_admin.credentials.Certificate('./auth/cs-webscraper.json')
        default_app = firebase_admin.initialize_app(cred_object, {
            'databaseURL': 'https://cs-webscraper-y10-default-rtdb.europe-west1.firebasedatabase.app/'
        })
        ref = db.reference('/auth')
        users = ref.get()
        usingFirebase = True
    except:
        with open('users.json', 'r+') as f:
            users = json.load(f)
        usingFirebase = False

    exist = Confirm.ask('Have you created an account here before?')

    if exist:
        exists(users)
    else:
        create = Confirm.ask('create one?')
        if create:
            createUser(users, usingFirebase, ref)
        else:
            return



if __name__ == '__main__':
    auth()