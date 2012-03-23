import os

# config
class Configuration(object):
# configure our database
    DATABASE = {
        'name': 'jamalong.db',
        'engine': 'peewee.SqliteDatabase',
        }
    DEBUG = True
    SECRET_KEY = 'ssshhhh123456789uuuuuuuuyyyyy'
    PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))
    SAVE_PATH = 'tmp/'
    UPLOADED_FILES_DEST = os.path.join(PROJECT_PATH, SAVE_PATH)
    ALLOWED_EXTENSIONS = {'mp3'}


