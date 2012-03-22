__author__ = 'orningvarasbjornsson'
import datetime

from flask import request, redirect, url_for, render_template, flash

from flask_peewee.utils import get_object_or_404, object_list

from app import app
from auth import auth
from models import Song

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
#@auth.login_required
def song_detail(id):
    song = get_object_or_404(Song.select().where(id=id))
    return render_template('song/detail.html', song=song)
