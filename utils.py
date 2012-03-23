import eyeD3
from app import app
from models import Song
import guitarparty

def process_mp3_song(path):
    tag = eyeD3.Tag()
    tag.link(path)
    song = Song()
    if tag.getTitle() and tag.getTitle() and tag.getAlbum() :
        song.title = tag.getTitle()
        song.artist = tag.getArtist()
        song.album = tag.getAlbum()
        song.path = path
        song.save()
        # TODO : Remove this test code
#        query_guitarparty_for_artist( tag.getArtist() )
#        query_guitarparty_for_song( tag.getTitle() )
        return 'ok'
    elif path:
        song.path = path
        song.save()
        return 'no tags'

def allowed_file(filename):
    return '.' in filename and\
        filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

def query_guitarparty_for_artist(artist):
    GP = guitarparty.Guitarparty()
    for artists in GP.get_query_artists( artist ):
        print artists['name'] + ' ' + artists['uri']

def query_guitarparty_for_song( song_title ):
    GP = guitarparty.Guitarparty()
    for song in GP.get_query_songs( song_title ):
        print song['title']

