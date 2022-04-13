from django import forms
from django.contrib.auth.models import User

from Users.models import WorkersModel, OrderModel


class WorkersForm(forms.ModelForm):
    class Meta:
        model = WorkersModel
        fields = ["rate_per_hour"]


class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderModel
        fields = ["user", "product", "how_math", "phone"]


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username"]

