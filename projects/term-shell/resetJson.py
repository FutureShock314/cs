import json

boilerPlate = json.dumps(
    {
        "username": "password",
        "nathan": "no"
    },
    indent=4
)

with open('./users.json', 'w') as f:
    f.write(boilerPlate)
