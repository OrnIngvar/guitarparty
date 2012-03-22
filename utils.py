import eyeD3
from models import Song

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
    print 'eyeD3'