from django.contrib.auth.models import User
from django.db import models


class SuppliersModel(models.Model):
    name = models.CharField(max_length=200)
    payment_deferment = models.IntegerField(default=0)

    def __str__(self):
        return f"id {self.id}: {self.name}: {self.payment_deferment}"


class ProductionModel(models.Model):
    name = models.CharField(max_length=200)
    size = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"id {self.id}: {self.name}: {self.size}: {self.price}"


class SupplyModel(models.Model):
    supplier = models.ForeignKey(SuppliersModel, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"id {self.id}: {self.supplier}: {self.date}: {self.amount}"


class WagesModel(models.Model):
    worker = models.ForeignKey(User, on_delete=models.CASCADE)
    date_from = models.DateField(null=True)
    date_to = models.DateField(null=True)
    hours = models.DecimalField(max_digits=5, decimal_places=2)
    total_wages = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"id {self.id}: {self.worker}: {self.date_from}: {self.date_to}: {self.hours}: {self.total_wages}"
