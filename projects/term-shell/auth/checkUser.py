from rich.prompt import Confirm
import getpass, json

def checkUser(username: str):
    with open('./users.json', 'r') as f:
        f = json.read()
        if username in f.keys():
            return True
        else:
            return False
