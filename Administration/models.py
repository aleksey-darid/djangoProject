from datetime import date

from django.db import models
from django.contrib.auth.models import User
from Users.models import WorkersModel


class ScheduleModel(models.Model):
    worker = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(null=True)
    time_from = models.TimeField(null=True)
    time_to = models.TimeField(null=True)
    delta = models.IntegerField(default=0)

    def __str__(self):
        return f"id {self.id}: {self.date}: {self.time_from}: {self.time_to}: {self.delta}"


date_today = date.today()


class BidModel(models.Model):
    data = models.DateField(default=f"{date_today}")
    text = models.CharField(max_length=200)

    def __str__(self):
        return f"id {self.id}: {self.data}: {self.text}"
