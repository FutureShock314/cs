from getpass import getpass

def exists(users: dict):
    password, username = '', ''

    while True:
        username = input('so what\'s your username then\n>> ')

        if username in users.keys():
            while password != users[username]:
                password = getpass('Password?\n>> ')
                if password != users[username]:
                    print('wrong lol')
                else:
                    print('ok') #! change to Welcome, {username}
                    return True
        else:
            print('username no exist lol')
            continue

        if password == users[username]:
            print('ok')
            return True
        else: continue
