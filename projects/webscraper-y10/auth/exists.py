from getpass import getpass

def exists(users: dict):
    password, username = '', ''

    while True:
        username = input('so what\'s your username then\n>> ')

        attempts = 0
        if username in users.keys():
            while password != users[username]:
                attempts += 1
                password = getpass('Password?\n>> ')
                if password == users[username]:
                    print('ok') #! change to Welcome, {username}
                    return True
                if attempts == 3:
                    print('too many wrong lol bye')
                    quit()
                if password != users[username]:
                    print('wrong lol')
        else:
            print('username no exist lol')
            continue

        if password == users[username]:
            print('ok')
            return True
        else: continue
