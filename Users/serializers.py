from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

from Users.models import OrderModel


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password", "email", "groups"]


class OrderSerializer(ModelSerializer):
    class Meta:
        model = OrderModel
        fields = ["user", "date", "num", "product", "how_math"]
