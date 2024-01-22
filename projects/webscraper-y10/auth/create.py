import firebase_admin, json
from firebase_admin import db
from getpass import getpass

def createUser(users: dict, usingFirebase = False, ref = '/auth', filePath = './users.json'):
    username, password = '', ''

    while username == '':
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

    if usingFirebase:
        ref = db.reference(f'/auth/{ username }')
        ref.set(password)

    if not usingFirebase:
        try:
            users[username] = password
            users = json.dumps(users, indent = 4)

            with open(filePath, 'w') as f:
                f.write(users)

            return True
        except:
            print('it no work :(')
            print('so i kick you >:(')
            quit()
