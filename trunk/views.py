import os
import datetime

from werkzeug.utils import secure_filename
from flask import request, redirect, url_for, render_template, flash
from flask_peewee.utils import get_object_or_404, object_list
from werkzeug.wrappers import Response

from app import app
from auth import auth
import guitarparty
from models import Song
from utils import process_mp3_song, allowed_file

# Initialize Guitarparty api
GP = guitarparty.Guitarparty()

@app.route('/')
def index(title=None):
    return render_template('index.html', title=title)

#@app.route('/songs/')
#def song_list():
#    allsongs = Song.select()
#    return object_list('song/index.html', allsongs)

#@app.route('/songs/<id>/')
#@auth.login_required
#def song_detail(id):
#    user = auth.get_logged_in_user()
#    print user
#    song = get_object_or_404(Song.select().where(id=id))
#    if song.title:
#        songlist = GP.get_query_songs( song.title )
#        print songlist
#    return render_template('song/detail.html', song=song)

# Assumed that we have the Guitarparty Id of a particular song with this route
@app.route('/api/gp/song/<id>')
def gp_song_detail(id):
    return GP.get_song( '/api/v2/songs/%s/' % (id) )

# Here we only have the title of the song to do a query
@app.route('/api/gp/songs/<title>')
def gp_song_query(title):
    return GP.get_query_songs(title)

@app.route('/api/songs/upload', methods=['POST'])
def upload_file():
    file = request.files.get('file')
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOADED_FILES_DEST'], filename))
        web_path = os.path.join(app.config['SAVE_PATH'], filename)
        if process_mp3_song(web_path) == 'ok':
            return Response('ok')
        else:
            return Response('song saved but no tags found. chords or lyrics will not be available')
    else:
        return Response('not a valid filetype')



