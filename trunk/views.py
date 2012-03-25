import os
import socket
from werkzeug.utils import secure_filename
from flask import request, render_template, send_from_directory
from werkzeug.wrappers import Response
from db import process_mp3_song
from app import app
import guitarparty
from utils import allowed_file

# Initialize Guitarparty api
GP = guitarparty.Guitarparty()

@app.route('/')
def index(title=None):
    return render_template('index.html', title=title)

# Assumed that we have the Guitarparty Id of a particular song with this route
@app.route('/api/gp/song/<id>')
def gp_song_detail(id):
    return GP.get_song( '/api/v2/songs/%s/' % id )

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

@app.route('/api/song/uploads/<filename>')
def uploaded_file(filename):
    try:
        file = send_from_directory(app.config['SAVE_PATH'], filename)
        return file
    except socket.error, e:
        print 'socket error in send_from_directory'
    except:
        print 'general exception'
