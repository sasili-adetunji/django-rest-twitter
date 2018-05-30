import tweepy
from tweepy import OAuthHandler
from rest_twitter.settings import (
    ACCESS_SECRET,
    ACCESS_TOKEN,
    CONSUMER_KEY,
    CONSUMER_SECRET
)
#
# CONSUMER_KEY = 'DrudfukhJJA3jLZrC0p8c7ROt'
# CONSUMER_SECRET = '8Dk2jp7EfN9KLOxuoRyTo7H03yugT5CQr69SGZsfm2D9Nq0sKg'
# ACCESS_TOKEN = '2732794984-iNz4Luc3IpOHU8XvD4wSYYRdemmJcC1WKlFxXXQ'
# ACCESS_SECRET = 'qopT46aEMQ1rtM9dZ0nqlP1gdVKVcLE8QviExr4xbLA5C'

def load_api():
    """Function that loads the twitter API after authorizing the user."""
    consumer_key = CONSUMER_KEY
    consumer_secret = CONSUMER_SECRET
    access_token = ACCESS_TOKEN
    access_token_secret = ACCESS_SECRET
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth)
