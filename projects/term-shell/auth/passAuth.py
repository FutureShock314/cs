import json, getpass

def passAuth(username: str):
    password = getpass.getpass('Please enter your password, you won\'t see it as it is inputted\n>> ', stream = None)
    with open('./users.json') as f:
        users = json.load(f)
    if users[username] == password:
        print('Password accepted.')
        return True
