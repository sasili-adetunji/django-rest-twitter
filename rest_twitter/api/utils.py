import tweepy
from tweepy import OAuthHandler
from rest_twitter.settings import (
    ACCESS_SECRET,
    ACCESS_TOKEN,
    CONSUMER_KEY,
    CONSUMER_SECRET
)


def load_api():
    """Function that loads the twitter API after authorizing the user."""

    consumer_key = CONSUMER_KEY
    consumer_secret = CONSUMER_SECRET
    access_token = ACCESS_TOKEN
    access_token_secret = ACCESS_SECRET
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth)
