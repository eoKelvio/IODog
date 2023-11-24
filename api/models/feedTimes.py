from django.db import models
from api.models.hours import Hours

class FeedTimes(models.Model):
    feed_time = models.ManyToManyField(Hours, related_name='feed_time')
    portion = models.IntegerField(null=False, blank=False)
    current_time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return super().__str__()
