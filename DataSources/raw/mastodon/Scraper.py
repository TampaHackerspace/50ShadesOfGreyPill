# uses https://github.com/halcy/Mastodon.py
# install by typing pip install Mastodon.py 

import sys
sys.path.append('c:/program files/anaconda3/lib/site-packages')
import codecs
import datetime
import json

from mastodon.Mastodon import Mastodon
from mastodon.streaming import StreamListener, MalformedEventError

__all__ = ['Mastodon', 'StreamListener', 'MalformedEventError']

## you need to create an app 
# Mastodon.create_app( 'softwerxpy', to_file = 'pytooter_clientcred.secret' )

## you need to create a secret key
# mastodon = Mastodon(client_id = 'pytooter_clientcred.secret')
# mastodon.log_in('<login>','<password>', to_file = 'pytooter_usercred.secret' )

mastodon = Mastodon(
    client_id = 'pytooter_clientcred.secret',
    access_token = 'pytooter_usercred.secret'
)
#mastodon.toot('my first Toot!')



class Listener(StreamListener):

    
    def __init__(self):
        self.updates = []
        self.notifications = []
        self.deletes = []
        self.heartbeats = 0
        print("_init_")

    def on_update(self, status):
        self.updates.append(status)
        print("on_update")
        filename = 'json_{:%Y%m%d%H%M%S%f}'.format(datetime.datetime.now())

        with open('data/' + filename + '.json', 'w') as outfile:
            json.dump(status, outfile)
    
    def on_notification(self, notification):
        self.notifications.append(notification)
        print("on_notification")

    def on_delete(self, status_id):
        self.deletes.append(status_id)
        print("on_delete")

    def handle_heartbeat(self):
        self.heartbeats += 1
        print("handle_heartbeat")

    def handle_stream_(self, lines):
        '''Test helper to avoid littering all tests with six.b().'''
        print("handle_stream_")
        return self.handle_stream(map(six.b, lines))

def test_heartbeat():
    listener = Listener()
    listener.handle_stream_([':one', ':two'])
    assert listener.heartbeats == 2


def test_status():
    listener = Listener()
    listener.handle_stream_([
        'event: update',
        'data: {"foo": "bar"}',
        '',
    ])
    assert listener.updates == [{"foo": "bar"}]


def test_notification():
    listener = Listener()
    listener.handle_stream_([
        'event: notification',
        'data: {"foo": "bar"}',
        '',
    ])
    assert listener.notifications == [{"foo": "bar"}]


def test_delete():
    listener = Listener()
    listener.handle_stream_([
        'event: delete',
        'data: 123',
        '',
    ])
    assert listener.deletes == [123]


l = Listener()
mastodon.public_stream(l)

input("Press Enter to continue...")
