import firebase_admin
from firebase_admin import db

class Database:

    def __init__(self, ref: str='/') -> None:
        self.ref = db.reference(ref)
        cred_object = firebase_admin.credentials.Certificate('./auth/cs-webscraper.json')
        default_app = firebase_admin.initialize_app(cred_object, {
            'databaseURL': 'https://cs-webscraper-y10-default-rtdb.europe-west1.firebasedatabase.app/'
        })

    def write(data: dict) -> bool:
        ...

    def read() -> dict:
        ...