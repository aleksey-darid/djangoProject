from rest_framework.serializers import ModelSerializer

from .models import SuppliersModel, ProductionModel, WagesModel, SupplyModel


class SupplySerializer(ModelSerializer):
    class Meta:
        model = SupplyModel
        fields = ["supplier", "date", "amount"]


class SuppliersSerializer(ModelSerializer):
    class Meta:
        model = SuppliersModel
        fields = ["name", "payment_deferment"]


class ProductionSerializer(ModelSerializer):
    class Meta:
        model = ProductionModel
        fields = ["name", "size", "price"]


class WagesSerializer(ModelSerializer):
    class Meta:
        model = WagesModel
        fields = ["worker", "date_from", "date_to", "hours", "total_wages"]
