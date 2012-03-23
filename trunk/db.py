import eyeD3
from models import Song

def process_mp3_song(path):
    tag = eyeD3.Tag()
    tag.link(path)
    song = Song()
    # Check if song is already in DB
    song_is_dupe = False
    song_exists = Song.select().where(path=path)
    for s in song_exists:
        s_id = s.id
        song_is_dupe = True

    if tag.getTitle() and tag.getTitle() and tag.getAlbum() and tag.getGenre() and not song_is_dupe:
        song.title = tag.getTitle()
        song.artist = tag.getArtist()
        song.album = tag.getAlbum()
        song.genre = tag.getGenre().getName()
        song.path = path
        song.save()
        return 'ok'
    # Song already exists in db so we only update the tags if by any chance the user updated them and uploaded again
    elif song_is_dupe:
        print 'song is duplicate'
        song.id = s_id
        song.title = tag.getTitle()
        song.artist = tag.getArtist()
        song.album = tag.getAlbum()
        song.genre = tag.getGenre().getName()
        print tag.getGenre().getName()
        song.update()
        return 'ok'
    elif path:
        song.path = path
        song.save()
        return 'no tags'
