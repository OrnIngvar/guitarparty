import eyeD3
from models import Song
import guitarparty

def process_mp3_song(path):
    tag = eyeD3.Tag()
    tag.link(path)
    print tag.getTitle()
    print tag.getArtist()
    print tag.getAlbum()
    song = Song()
    song.title = tag.getTitle()
    song.artist = tag.getArtist()
    song.album = tag.getAlbum()
    song.path = path
    song.save()

    GP = guitarparty.Guitarparty()
    for artists in GP.get_query_artists( tag.getArtist() ):
        print artists['name'] + artists['uri']

