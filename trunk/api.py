from flask_peewee.rest import RestAPI, UserAuthentication

from app import app
from auth import auth
from models import Song

user_auth = UserAuthentication(auth)

# instantiate our api wrapper
api = RestAPI(app, default_auth=user_auth)

api.register(Song)

# get all songs : /api/song
# get a single song : /api/song/<id>

# upload a song : /api/song/upload

# filter by artist name : /api/song/?artist=Mugison
# filter by song title : /api/song/?title=Stingum af
# or
# /api/song/?title__eq=Stingum+af

# filter by album name : /api/song/?album=Mugiboogie

# filter by artist starts with : /api/song/?artist__istartswith=Mugi
# filter by artist name contains : /api/song/?artist__icontains=Mug

# sort by created date desc : /api/song/?genre__eq=Rock&ordering=created
# sort by created date desc : /api/song/?genre__eq=Rock&ordering=-created

# limit results : /api/song/?limit=1
