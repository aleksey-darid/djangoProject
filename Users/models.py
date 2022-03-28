from django.contrib.auth.models import User
from django.db import models

from Management.models import ProductionModel


class WorkersModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rate_per_hour = models.IntegerField(default=5)

    def __str__(self):
        return f"id {self.id}: {self.user}: {self.rate_per_hour}:"


class ManagerModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()

    def __str__(self):
        return f"id {self.id}: {self.user}: {self.email}:"


class OrderModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    num = models.IntegerField()
    product = models.ForeignKey(ProductionModel, on_delete=models.CASCADE)
    how_math = models.IntegerField()

    def __str__(self):
        return f"id {self.id}: {self.user}: {self.date}: {self.num}: {self.product}: {self.how_math}:"
