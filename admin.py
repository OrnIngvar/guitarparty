from flask_peewee.admin import Admin, ModelAdmin

from app import app
from auth import auth
from models import Song

class SongAdmin(ModelAdmin):
    columns = ('title', 'artist', 'album', 'genre', 'path', 'created',)

admin = Admin(app, auth)
admin.register(Song, SongAdmin)
auth.register_admin(admin)


