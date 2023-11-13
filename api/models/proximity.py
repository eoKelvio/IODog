from django.db import models

class Proximity (models.Model):
    is_close = models.BooleanField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return super().__str__() 