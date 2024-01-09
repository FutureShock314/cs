import firebase_admin, json
from firebase_admin import db

cred_object = firebase_admin.credentials.Certificate('./cs-firebase-test.json')
default_app = firebase_admin.initialize_app(cred_object, {
	'databaseURL': 'https://cs-firebase-test-7f9d5-default-rtdb.europe-west1.firebasedatabase.app/'
})

ref = db.reference('/')

with open('test.json', 'r') as f:
	test = json.load(f)
# ref.set(test)

get = ref.get()

print(get)
