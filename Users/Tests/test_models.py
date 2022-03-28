from django.contrib.auth.models import User
from rest_framework.test import APITestCase

from Management.models import ProductionModel
from Users.models import WorkersModel, ManagerModel, OrderModel


class HRApiTestCase(APITestCase):
    def test_WorkersModel(self):
        user1 = User.objects.create(username="test1", password="test1")
        user2 = User.objects.create(username="test2", password="test2")
        w1 = WorkersModel.objects.create(user=user1, rate_per_hour=5)
        w2 = WorkersModel.objects.create(user=user2, rate_per_hour=4)

    def test_ManagerModel(self):
        user1 = User.objects.create(username="test1", password="test1")
        user2 = User.objects.create(username="test2", password="test2")
        m1 = ManagerModel.objects.create(user=user1, email="test1@gmail.com")
        m2 = ManagerModel.objects.create(user=user2, email="test2@gmail.com")

    def test_OrderModel(self):
        user1 = User.objects.create(username="test1", password="test1")
        user2 = User.objects.create(username="test2", password="test2")
        pr1 = ProductionModel.objects.create(name="test1", size=250, price=125.50)
        pr2 = ProductionModel.objects.create(name="test2", size=1000, price=12.50)
        ord1 = OrderModel.objects.create(user=user1, date="2022-03-21 01:00:00", num=1, product=pr1, how_math=1)
        ord2 = OrderModel.objects.create(user=user2, date="2022-03-22 02:00:00", num=2, product=pr2, how_math=2)
