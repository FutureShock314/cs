import firebase_admin, json
from firebase_admin import db
from getpass import getpass

def createUser(users: dict, usingFirebase, ref = '/auth'):
    username, password = '', ''

    while username == '':
        username = input('What would you like your username to be?\n>> ')
        if username == '' or len(username) < 3:
            print('Username is either less than 3 characters or non existent, this ain\'t allowed mate')

    while password != '':
        password = getpass('Password?\n>> ')
        if password == '':
            print('cant have empty password')

    if usingFirebase:
        ref.set({ username: password })

