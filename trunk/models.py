__author__ = 'orningvarasbjornsson'

import datetime

from flask_peewee.auth import BaseUser
from peewee import *

from app import db

class User(db.Model, BaseUser):
    username = CharField()
    password = CharField()
    email = CharField()
    active = BooleanField(default=True)
    admin = BooleanField(default=False)

    def __unicode__(self):
        return self.username

class Song(db.Model):
    title = TextField()
    artist = TextField()
    album = TextField()
    created = DateTimeField(default=datetime.datetime.now)

