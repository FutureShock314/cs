def auth():
    username = input('username: ')

    with open('./users.json') as f:
        while username == '':
            username = input('username: ')
        if username in json.load(f).keys():
            password = input('password: ')
        else:
            print('no user found')
        while password = '':
            password = input('password: ')

        if password == json.load(f)[username]:
            continue
        else:
