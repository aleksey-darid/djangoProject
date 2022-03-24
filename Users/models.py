from django.contrib.auth.models import User
from django.db import models


class Workers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rate_per_hour = models.IntegerField(default=5)

    def __str__(self):
        return f"id {self.id}: {self.user}: {self.rate_per_hour}:"
