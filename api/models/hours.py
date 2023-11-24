from django.db import models

class Hours(models.Model):
    times = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self) -> str:
        return super().__str__()