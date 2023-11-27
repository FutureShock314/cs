import json
from auth import auth
from rich.prompt import Confirm


# with open('./users.json', 'r') as f:
#     users = json.load(f)
# users["nathan"] = "password"
# users = json.dumps(users, indent=4)

# with open('./users.json', 'w') as f:
#     f.write(users)

auth = auth.auth()
username = auth[1]
print(auth)
print(username)
if auth[0]:
    print('Logged in!')
