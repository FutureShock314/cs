import firebase_admin

cred_object = firebase_admin.credentials.Certificate(....file)
default_app = firebase_admin.initialize_app(cred_object, {
	'databaseURL':databaseURL
})
