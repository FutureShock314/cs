import json

boilerPlate = json.dumps(
    {
        "root": "superSecurePassword",
        "username": "password",
        "nathaniel": "no"
    },
    indent=4
)

with open('./users.json', 'w') as f:
    f.write(boilerPlate)
