import json
from auth import auth
from rich.prompt import Confirm


# with open('./users.json', 'r') as f:
#     users = json.load(f)
# users["nathan"] = "password"
# users = json.dumps(users, indent=4)

# with open('./users.json', 'w') as f:
#     f.write(users)

if auth.auth():
    print('Logged in!')