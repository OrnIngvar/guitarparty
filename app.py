import datetime
from flask import Flask
from flask.templating import render_template
from flask_peewee.auth import Auth
from flask_peewee.db import Database
from flask_peewee.utils import get_object_or_404, object_list
from peewee import *
from flask_peewee.admin import Admin, ModelAdmin
from flask_peewee.rest import RestAPI, UserAuthentication

import guitarparty
guitarparty.api_key = 'f97a2b52acb6878a5ba3b19f2e78b7a28d831897'
GP = guitarparty.Guitarparty()

#GP.create_songbook('Ernies songbook')

for songbook in GP.get_songbooks():
    print songbook['title'] + songbook['uri']

for song in GP.get_query_songs('Jolene'):
    print song['body'] +  ' ' + song['title'] + ' ' + song['uri']

song = GP.get_song('/api/v2/songs/3207/')
print song

for artists in GP.get_query_artists('Dolly Parton'):
    print artists['name'] + artists['uri']

artist = GP.get_artist('/api/v2/artists/1/')
print artist

# configure our database
DATABASE = {
    'name': 'jamalong.db',
    'engine': 'peewee.SqliteDatabase',
    }
DEBUG = True
SECRET_KEY = 'ssshhhh123456789uuuuuuuuyyyyy'

app = Flask(__name__)
app.config.from_object(__name__)

# instantiate the db wrapper
db = Database(app)

#Models
class Song(db.Model):
    title = TextField()
    artist = TextField()
    album = TextField()
    created = DateTimeField(default=datetime.datetime.now)

class SongAdmin(ModelAdmin):
    columns = ('title', 'artist', 'album', 'created',)

# create an Auth object for use with our flask app and database wrapper
auth = Auth(app, db)
admin = Admin(app, auth)
admin.register(Song, SongAdmin)
auth.register_admin(admin)

admin.setup()

# instantiate the user auth
user_auth = UserAuthentication(auth)

# create a RestAPI container
api = RestAPI(app, default_auth=user_auth)
api.register(Song)

api.setup()

@app.route('/')
def index(title=None):
#    return 'JamAlong'
#    title = 'JamAlong'
    return render_template('base.html', title=title)

@app.route('/songs/')
def song_list():
    allsongs = Song.select()
    return object_list('song/index.html', allsongs)


@app.route('/songs/<int:id>/')
def song_detail(id):
    song = get_object_or_404(Song.select().where(id=id), id=id)
    return render_template('song/detail.html', song=song)

if __name__ == '__main__':
    auth.User.create_table(fail_silently=True)
    Song.create_table(fail_silently=True)

    app.run()