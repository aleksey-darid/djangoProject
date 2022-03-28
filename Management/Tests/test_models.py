from django.contrib.auth.models import User
from rest_framework.test import APITestCase

from Management.models import SuppliersModel, ProductionModel, SupplyModel, WagesModel
from Users.models import WorkersModel


class HRApiTestCase(APITestCase):
    def test_SuppliersModel(self):
        suppli1 = SuppliersModel.objects.create(name="test1", payment_deferment=7)
        suppli2 = SuppliersModel.objects.create(name="test2", payment_deferment=20)

    def test_ProductionModel(self):
        pr1 = ProductionModel.objects.create(name="test1", size=250, price=125.50)
        pr2 = ProductionModel.objects.create(name="test2", size=1000, price=12.50)

    def test_SupplyModel(self):
        suppli1 = SuppliersModel.objects.create(name="test1", payment_deferment=7)
        suppli2 = SuppliersModel.objects.create(name="test2", payment_deferment=20)
        supply1 = SupplyModel.objects.create(supplier=suppli1, date="2022-03-01", amount=349.54)
        supply2 = SupplyModel.objects.create(supplier=suppli2, date="2022-03-02", amount=120.23)

    def test_WagesModel(self):
        user1 = User.objects.create(username="test1", password="test1")
        user2 = User.objects.create(username="test2", password="test2")
        wag1 = WagesModel.objects.create(worker=user1, date_from="2022-03-01", date_to="2022-03-20", hours=210.5,
                                         total_wages=1020.98)
        wag2 = WagesModel.objects.create(worker=user2, date_from="2022-03-02", date_to="2022-03-22", hours=110.5,
                                         total_wages=620.98)
