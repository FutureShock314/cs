import json
from rich.prompt import Confirm

confirm = Confirm.ask('Are you sure?')

boilerPlate = json.dumps(
    {
        "root": "superSecurePassword",
        "username": "password",
        "nathaniel": "no"
    },
    indent=4
)

with open('./users.json', 'w') as f:
    if confirm:
        f.write(boilerPlate)
    else:
        print('you said no so bye bye')
