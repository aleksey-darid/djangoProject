from datetime import date

from django.test import TestCase

from Management.models import SuppliersModel, SupplyModel


class ManagerTestCase(TestCase):

    def test_SuppliersViews(self):
        response = self.client.get('/suppliers_page/')
        self.assertEqual(response.status_code, 200)
        response_post = self.client.post('/suppliers_add/', {"add": "add", "name": "test", "pay_def": 7})
        self.assertEqual(response_post.status_code, 302)
        response_post = self.client.post('/suppliers_del/', {"del": "del", "del_name": 1})
        self.assertEqual(response_post.status_code, 302)
        SuppliersModel.objects.create(name="test", id=1, payment_deferment=7)
        response_post = self.client.post('/suppliers_put/',
                                         {"put": "put", "put_name": 1, "name": "test", "pay_def_put": 7})
        self.assertEqual(response_post.status_code, 302)

    def test_ProductionViews(self):
        response = self.client.get('/production_page/')
        self.assertEqual(response.status_code, 200)

    def test_SupplyViews(self):
        response = self.client.get('/supply_page/')
        self.assertEqual(response.status_code, 200)
        sup = SuppliersModel.objects.create(name="test", id=1, payment_deferment=7)
        response_post = self.client.post('/supply_add/', {"add": "add", "sup": 1, "dat": date.today(), "amo": 200})
        self.assertEqual(response_post.status_code, 302)
        response_post = self.client.post('/supply_del/', {"del": "del", "del_id": 1})
        self.assertEqual(response_post.status_code, 302)
        SupplyModel.objects.create(supplier=(SuppliersModel.objects.get(id=sup.id)), date=date.today(), amount=200, id=1)
        response_post = self.client.post('/supply_put/',
                                         {"put": "put", "put_id": 1, "sup": 1, "dat": date.today(), "amo": 200})
        self.assertEqual(response_post.status_code, 302)

    def test_WagesViews(self):
        response = self.client.get('/wages_page/')
        self.assertEqual(response.status_code, 200)
        response_post = self.client.post('/wages_page/', {"worker": 1})
        self.assertEqual(response_post.status_code, 200)

    def test_LookOrderViews(self):
        response = self.client.get('/look_order_page/')
        self.assertEqual(response.status_code, 200)

    def test_LookBidViews(self):
        response = self.client.get('/look_bid_page/')
        self.assertEqual(response.status_code, 200)
