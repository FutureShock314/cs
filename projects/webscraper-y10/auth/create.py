import firebase_admin, json
from getpass import getpass
try:
    # from auth import db as database
    from database import Db as database
except:
    # from auth.auth import db as database
    from auth.database import Db as database

def createUser(users: dict, filePath = './users.json'):
    username, password = '', ''

    while username == '' or len(username) < 3:
        username = input('What would you like your username to be?\n>> ')
        if username == '' or len(username) < 3:
            print('Username is either less than 3 characters or non existent, this ain\'t allowed mate')
        if username in users.keys():
            print('WOAH WOAH WOAH that name already exists')
            print('better go login, im removing you from this program >:(')
            quit()

    while password == '':
        password = getpass('Password?\n>> ')
        if password == '':
            print('cant have empty password')

    if database.usingFirebase:
        database.addUser({username: password})

    if not database.usingFirebase:
        try:
            database.addUserJson({username: password}, './users.json')
        except:
            print('it no work :(')
            print('so i kick you >:(')
            quit()
