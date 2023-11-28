import json
from auth import auth
from rich.prompt import Confirm

auth = auth.auth()
username = auth[1]
print(auth)
print(username)
if auth[0]:
    print('Logged in!')
if auth[1] == 'root':
    print('sudo/root access enabled.')
