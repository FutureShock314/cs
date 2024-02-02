import firebase_admin, json
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
            if str(self.ref).endswith('/'):
                self.ref = db.reference(f'{self.str_ref}{username}/')
            else:
                self.ref = db.reference(f'{self.str_ref}/{username}/')

            self.ref.set(userData[username])
        else:
            print('Successfully added user(s)!')
            return True

    def addJson(self, userData: dict, filePath: str) -> bool:
        ...

    def readUsers(self) -> dict:
        if not self.usingFirebase:
            print('Firebase is not connected, can\'t do this :(')
            return
        ...

    def readJson(self, filePath: str) -> dict:
        ...

if __name__ == '__main__':
    db = Database('/auth/')
    db.addUser({'username here': 'password here'})
