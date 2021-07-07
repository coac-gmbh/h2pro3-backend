import firebase_admin
from firebase_admin import credentials, auth, firestore
from django.conf import settings


def initialize_firebase_app():
    if len(firebase_admin._apps) == 0:
        cred = credentials.Certificate(settings.FIREBASE_CREDENTIALS_PATH)
        firebase_admin.initialize_app(cred)


def firebase_db():
    initialize_firebase_app()
    # One-time configuration and initialization.
    db = firestore.client()
    return db


def create_firebase_token(user):
    initialize_firebase_app()
    if user.is_authenticated:
        if not get_firebase_user_data(user):
            update_or_create_firebase_user(user)
        uid = str(user.username)
        firebase_token = auth.create_custom_token(uid)
        return firebase_token
    return None


def get_firebase_user_data(user):
    db = firebase_db()
    user_ref = db.collection(u'users').document(str(user.username))
    user_data = user_ref.get()
    return user_data.to_dict()


def set_firebase_user_data(user):
    if not hasattr(user, 'profile'):
        return
    db = firebase_db()
    doc_ref = db.collection(u'users').document(str(user.username))
    # TODO: complete set fields fot tinder module
    doc_ref.set({
        'firstName': user.profile.name if user.profile else '',
        'email': user.email,
        'id': str(user.id),
        'username': str(user.username),
        'showMe': True
    })


def update_or_create_firebase_user(user):
    initialize_firebase_app()
    uid = str(user.username)
    user_data = {'display_name': user.username}
    if user.email != "":
        user_data['email'] = user.email
    if user.get_full_name() != "":
        user_data['display_name'] = user.get_full_name()
    try:
        auth.update_user(uid, **user_data)
    except auth.UserNotFoundError:
        auth.create_user(uid=uid, **user_data)
    except Exception as e:
        raise e
    set_firebase_user_data(user)
