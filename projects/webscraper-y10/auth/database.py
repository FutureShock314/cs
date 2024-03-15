import firebase_admin, json, os
from firebase_admin import db
class Database:

    def __init__(self, cred_path: str = './auth/cs-webscraper.json', auth_ref: str = '/') -> None:
        try:
            cred_object = firebase_admin.credentials.Certificate(cred_path)
            default_app = firebase_admin.initialize_app(cred_object, {
                'databaseURL': 'https://cs-webscraper-y10-default-rtdb.europe-west1.firebasedatabase.app/'
            })
            self.auth_ref = db.reference(auth_ref)
            self.usingFirebase = True
        except:
            print('err')
            self.usingFirebase = False
        self.str_ref = auth_ref
        # print('Initialised!')

    def usingFirebase(self):
        return self.usingFirebase

    def addUser(self, userData: dict) -> bool:
        '''
            Adds user(s) to the database at the path specified + /{username}
        '''
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

    def getUsers(self) -> dict:
        if not self.usingFirebase:
            print('Firebase is not connected, can\'t do this :(')
            return

        users = self.auth_ref.get()
        # print(users)
        return users

    def getUsersJson(self, filePath: str) -> dict:
        if not os.path.exists(filePath):
            print(f'File {filePath} does not exist.')
            return

        with open(filePath, 'r') as f:
            users = json.load(f)
            print(users)
            return users

    def writeDataJson(
        self,
        path: str,
        data: dict,
        # type_: str
    ) -> None:
        # if type_ not in {'w', 'n'}:
        #     raise ValueError(f'At parameter \'type_\': expected [\'w\', \'n\'], got \'{type_}\'')

        if json.load(open(path, 'r')):
          print('Data already saved, exiting...')
      
        with open(path, 'w') as f:
            data = json.dumps(data, indent = 4)
            f.write(data)


Db = Database(cred_path = './auth/cs-webscraper.json', auth_ref = '/auth/')

if __name__ == '__main__':
    db = Database('/auth/')
    db.addUser({'username here': 'password here'})
