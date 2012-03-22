__author__ = 'orningvarasbjornsson'

# config
class Configuration(object):
# configure our database
    DATABASE = {
        'name': 'jamalong.db',
        'engine': 'peewee.SqliteDatabase',
        }
    DEBUG = True
    SECRET_KEY = 'ssshhhh123456789uuuuuuuuyyyyy'
