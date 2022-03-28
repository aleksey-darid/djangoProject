from django import forms
from .models import ProductionModel, SupplyModel, SuppliersModel, WagesModel


class ProductionForm(forms.ModelForm):
    class Meta:
        model = ProductionModel
        fields = ["name", "size", "price"]


class SupplyForm(forms.ModelForm):
    class Meta:
        model = SupplyModel
        fields = ["supplier", "date", "amount"]
        widgets = {"date": forms.SelectDateWidget}


class SuppliersForm(forms.ModelForm):
    class Meta:
        model = SuppliersModel
        fields = ["name", "payment_deferment"]


class WagesForm(forms.ModelForm):
    class Meta:
        model = WagesModel
        fields = ["worker", "date_from", "date_to"]
        widgets = {"date_from": forms.SelectDateWidget,
                   "date_to": forms.SelectDateWidget}