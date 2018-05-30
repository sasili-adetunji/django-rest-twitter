import tweepy
from rest_framework.views import APIView, status
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from .utils import load_api
from .serializers import TweetSerializer, UserProfileSerializer, TokenSerializer
from .permissions import UserProfilePermission
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.settings import api_settings
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import authenticate, login
from .models import UserProfile


jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class UserProfileViewSet(ModelViewSet):
    """
    Handles creating reading and updating of user profiles
    """

    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (UserProfilePermission,)
    http_method_names = ['post', 'put']


class LoginViewSet(ViewSet):
    """ checks email and password and return auth token """

    serializer_class = AuthTokenSerializer

    def create(self, request):
        """ Use the ObtainAuthToken APIView to validate and create a token """

        username = request.data.get('username', '')
        password = request.data.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # login saves the user’s ID in the session,
            # using Django’s session framework.
            login(request, user)
            serializer = TokenSerializer(data={
                # using drf jwt utility functions to generate a token
                'token': jwt_encode_handler(
                    jwt_payload_handler(user)
                )})
            serializer.is_valid()

            return Response(serializer.data)
        return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class UserTweetView(APIView):

    serializer_class = TweetSerializer
    permission_classes = (UserProfilePermission,)

    def post(self, request):
        """
        Create a new tweet
        This view function creates/POSTs a new tweet for the user.
        """
        tweets = request.data.get('tweets', None)
        if tweets is not None:
            api = load_api(request)
            try:
                api.update_status(tweets)
            except tweepy.TweepError as e:
                return Response({"message": e.args[0][0]['message']}, status=status.HTTP_400_BAD_REQUEST)
            return Response({"message": "Your tweets has been updated"}, status=status.HTTP_201_CREATED)

    def get(self, request):
        """
        Get the user's tweets
        This view function gets all the users tweets on the timeline
        """

        api = load_api(request)
        try:
            my_tweets = api.user_timeline()
        except tweepy.TweepError as e:
            return Response({"message": e.args[0][0]['message']}, status=status.HTTP_400_BAD_REQUEST)
        tweet_list = []
        for tweet in my_tweets:
            tweet_list.append(tweet.text)
        return Response({'message': tweet_list}, status=status.HTTP_200_OK)
