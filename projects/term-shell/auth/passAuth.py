import json, getpass

def passAuth(username: str):
    password = ''
    with open('./users.json') as f:
        users = json.load(f)
    while users[username] != password:
        password = getpass.getpass('Please enter your password, you won\'t see it as it is inputted, or press CTRL+C to quit.\n>> ', stream = None)
        if users[username] == password:
            print('Password accepted.')
            return True
        else:
            print('Incorrect password.')
