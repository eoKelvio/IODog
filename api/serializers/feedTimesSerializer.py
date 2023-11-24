from rest_framework import serializers
from api.models.feedTimes import FeedTimes
from api.serializers.hoursSerializer import HoursSerializer

class FeedTimesSerializer(serializers.ModelSerializer):

    feed_time = serializers.SlugRelatedField(
        many=True,
        read_only = True,
        slug_field='times'
    )

    class Meta:
        model = FeedTimes
        fields = ['id', 'portion', 'current_time', 'feed_time']