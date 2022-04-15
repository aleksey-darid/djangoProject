from Management.views import Suppliers
from rest_framework.test import APITestCase, APIRequestFactory


class ManagerTestCase(APITestCase):

    def test_SuppliersViews(self):
        s = Suppliers()
        factory = APIRequestFactory()
        request = factory.get("/suppliers_app_/")
        s.suppliers_get(request)
        request = factory.post("/suppliers_get/", {"name": "1", "pay_def": "7"})
        s.suppliers_add(request)
        s.suppliers_del(request)
        s.suppliers_put(request)

    def test_ProductionViews(self):
        pass

    def test_SupplyViews(self):
        pass

    def test_WagesViews(self):
        pass

    def test_LookOrderViews(self):
        pass

    def test_LookBidViews(self):
        pass
