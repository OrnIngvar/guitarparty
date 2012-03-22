import os
import datetime

from werkzeug.utils import secure_filename
from flask import request, redirect, url_for, render_template, flash
from flask_peewee.utils import get_object_or_404, object_list
from werkzeug.wrappers import Response

from app import app
from auth import auth
from models import Song
from utils import process_mp3_song


def allowed_file(filename):
    return '.' in filename and\
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index(title=None):
#    return 'JamAlong'
#    title = 'JamAlong'
    return render_template('index.html', title=title)

@app.route('/songs/', methods=['GET', 'POST'])
def song_list():
    allsongs = Song.select()
    return object_list('song/index.html', allsongs)


@app.route('/songs/<id>/')
@auth.login_required
def song_detail(id):
    user = auth.get_logged_in_user()
    print user
    song = get_object_or_404(Song.select().where(id=id))
    return render_template('song/detail.html', song=song)

@app.route('/api/songs/upload', methods=['POST'])
def upload_file():
    file = request.files.get('file')
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOADED_FILES_DEST'], filename))
        fullpath = os.path.join(app.config['UPLOADED_FILES_DEST'], filename)
        process_mp3_song(fullpath)
        return Response('ok')
    else:
        return 404


