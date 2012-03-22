from flask_peewee.rest import RestAPI, RestResource, UserAuthentication, AdminAuthentication, RestrictOwnerResource

from app import app
from auth import auth
from models import Song

user_auth = UserAuthentication(auth)

# instantiate our api wrapper
api = RestAPI(app, default_auth=user_auth)

api.register(Song)

