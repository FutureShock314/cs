import json
from auth import auth
from rich.prompt import Confirm

auth = auth.auth()

if auth[0] == False:
    quit()

username = auth[1] or None
print(auth)
print(username)

if auth[0]:
    print('Logged in!')
else:
    print('bro you did the only thing that was capable of logging out')
    print('you deserve this')
    quit()

if auth[1] == 'root':
    print('sudo/root access enabled.')
