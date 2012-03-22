import datetime
from peewee import *

from app import db

class Song(db.Model):
    title = TextField()
    artist = TextField()
    album = TextField()
    created = DateTimeField(default=datetime.datetime.now)

