import requests
import logging

try:
    import json
except ImportError:
    import simplejson as json

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

host = 'http://www.guitarparty.com'
api_endpoint = '/api/v2'
api_key = 'f97a2b52acb6878a5ba3b19f2e78b7a28d831897'

def deserialize(raw_data):
    data = json.loads(raw_data)
    if 'objects' in data.keys():
        return data['objects']
    else:
        return data

class Guitarparty(object):
    def __init__(self, api_key=None, host=None):
        _globals = globals()
        self.host = host or _globals['host']
        self.api_key = api_key or _globals['api_key']
        self.api_endpoint = api_endpoint or _globals['api_endpoint']
        self.url = '%s%s' % (self.host, self.api_endpoint)
        self.head = { 'Guitarparty-Api-Key' : self.api_key }

    def get_query_songs(self, query):
        url = '%s/songs/?query=%s&' % (self.url, query)
        r = self.make_request( 'get', url , headers=self.head )
        return r.content

    def get_song(self, uri):
        url = '%s%s' % (self.host, uri)
        r = self.make_request( 'get', url )
        return r.content

    def get_query_artists(self, query):
        url = '%s/artists/?query=%s&' % (self.url, query)
        r = self.make_request( 'get', url , headers=self.head )
        return deserialize( r.content )

    def get_artist(self, uri):
        url = '%s%s' % (self.host, uri)
        r = self.make_request( 'get', url )
        return deserialize(r.content)

    def get_songbooks(self):
        url = '%s/songbooks/' % self.url
        r = self.make_request('get', url)
        return deserialize(r.content)

    def get_songbook(self, uri):
        url = '%s%s' % (self.host, uri)
        r = self.make_request('get', url)
        return deserialize(r.content)

    def create_songbook(self, title, description=None, is_public=False):
        url = '%s/songbooks/' % self.url
        data = {
            'title': title,
            'description': description,
            'is_public': is_public,
            }
        r = self.make_request('post', url, data=json.dumps(data))
        return deserialize(r.content)

    def get_songbook_songs(self, sb_uri):
        url = '%s%ssongs/' % (self.host, sb_uri)
        r = self.make_request('get', url)
        return deserialize(r.content)

    def get_songbook_songitem(self, uri):
        url = '%s%s' % (self.host, uri)
        r = self.make_request('get', url)
        return deserialize(r.content)

    def delete_songbook(self, uri):
        url = '%s%s' % (self.host, uri)
        r = self.make_request('delete', url)
        if r.status_code == 204:
            return True
        return False

    def make_request(self, method, uri, **kwargs):
        return requests.request(method, uri + '?api_key=' + self.api_key, **kwargs)


