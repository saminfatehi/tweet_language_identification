from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time

access_token = "...."
access_token_secret = "...."
consumer_key = "...."
consumer_secret = "...."

class Listener(StreamListener):

    def on_data(self, data):
        try:
            print data
            return True
        except BaseException,e:
            print "failed"

    def on_error(self, status_code):
        print status_code

l = Listener()
a = OAuthHandler(consumer_key, consumer_secret)
a.set_access_token(access_token, access_token_secret)
stream = Stream(a,l)
stream.filter(track=["i"])
