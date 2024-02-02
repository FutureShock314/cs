import firebase_admin, json, os
from firebase_admin import db

class Database:

    def __init__(self, cred_path: str = './auth/cs-webscraper.json', ref: str = '/') -> None:
        self.cred_path = cred_path
        try:
            cred_object = firebase_admin.credentials.Certificate(self.cred_path)
            default_app = firebase_admin.initialize_app(cred_object, {
                'databaseURL': 'https://cs-webscraper-y10-default-rtdb.europe-west1.firebasedatabase.app/'
            })
            self.ref = db.reference(ref)
            self.usingFirebase = True
        except:
            self.usingFirebase = False
        self.str_ref = ref
        print('Initialised!')

    def addUser(self, userData: dict) -> bool:
        if not self.usingFirebase:
            print('Firebase is not connected, can\'t do this :(')
            return
        for username in userData:
            if self.str_ref.endswith('/'):
                ref = db.reference(f'{self.str_ref}{username}/')
            else:
                ref = db.reference(f'{self.str_ref}/{username}/')

            ref.set(userData[username])
        else:
            print('Successfully added user(s)!')
            return True

    def addUserJson(self, userData: dict, filePath: str) -> bool:
        if not os.path.exists(filePath):
            with open(filePath, 'w') as f:
                ...
        with open(filePath, 'r') as f:
            existingData = json.load(f)

        for username in userData:
            existingData[username] = userData[username]

        existingData = json.dumps(existingData, indent = 4)
        with open(filePath, 'w') as f:
            f.write(existingData)

    def readUsers(self) -> dict:
        if not self.usingFirebase:
            print('Firebase is not connected, can\'t do this :(')
            return

        users = self.ref.get()
        print(users)
        return users

    def readUsersJson(self, filePath: str) -> dict:
        if not os.path.exists(filePath):
            print(f'File {filePath} does not exist.')
            return

        with open(filePath, 'r') as f:
            users = json.load(f)
            print(users)
            return users


if __name__ == '__main__':
    db = Database('/auth/')
    db.addUser({'username here': 'password here'})
