from django.shortcuts import render
from rest_framework.views import APIView, status
from rest_framework.response import Response
from .utils import load_api
from .serializers import TweetSerializer


class UserTweetView(APIView):

    serializer_class = TweetSerializer

    def post(self, request):
        """
        Create a new tweet
        This view function creates/POSTs a new tweet for the user.
        """
        tweets = request.data.get('tweets', None)
        if tweets is not None:
            api = load_api()
            try:
                api.update_status(tweets)
            except Exception:
                return Response({"message": "You can not update an empty tweet"}, status=status.HTTP_400_BAD_REQUEST)
            return Response({"message": "Your tweets has been updated"}, status=status.HTTP_201_CREATED)

    def get(self):
        """
        Get the user's tweets
        This view function gets all the users tweets on the timeline
        """
        api = load_api()
        my_tweets = api.user_timeline()
        tweet_list = []
        for tweet in my_tweets:
            tweet_list.append(tweet.text)
        return Response({'message': tweet_list}, status=status.HTTP_200_OK)
