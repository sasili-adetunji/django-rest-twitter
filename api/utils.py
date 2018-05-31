from tweepy import OAuthHandler, API


def load_api(request):

    """Function that loads the twitter API after authorizing the user."""
    consumer_key = request.user.consumer_key
    consumer_secret = request.user.consumer_secret
    access_token = request.user.oauth_token
    access_token_secret = request.user.oauth_token_secret
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return API(auth)
