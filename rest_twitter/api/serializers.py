from rest_framework import serializers


class TweetSerializer(serializers.Serializer):
    """
    This serializer serializes the tweets data
    """
    tweets = serializers.CharField(max_length=255)
