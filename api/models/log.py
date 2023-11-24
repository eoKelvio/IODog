from django.db import models

class Log(models.Model):
    food_liberation = models.BooleanField(null=False, blank=False)
    portions = models.IntegerField(null=False, blank=False)
    food_level = models.CharField(max_length=5, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return super().__str__()