from datetime import date

from django.contrib.auth.models import User
from rest_framework.test import APITestCase

from Administration.models import ScheduleModel, BidModel


class HRApiTestCase(APITestCase):
    def test_ScheduleModel(self):
        user1 = User.objects.create(username="test1", password="test1")
        user2 = User.objects.create(username="test2", password="test2")
        sh1 = ScheduleModel.objects.create(worker=user1, date="2022-03-01", time_from="21:00:00", time_to="23:00:00",
                                           delta=7.5)
        sh2 = ScheduleModel.objects.create(worker=user2, date="2022-03-02", time_from="20:00:00", time_to="22:00:00",
                                           delta=14.5)

    def test_BidModel(self):
        date_today = date.today()
        b1 = BidModel.objects.create(data=date_today, text="test 1, test 1")
        b2 = BidModel.objects.create(data="2022-03-02", text="test 2, test 2")
