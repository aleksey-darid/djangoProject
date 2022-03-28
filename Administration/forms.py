from django import forms
from .models import ScheduleModel, BidModel


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = ScheduleModel
        fields = ["date", "time_from", "time_to"]


class BidForm(forms.ModelForm):
    class Meta:
        model = BidModel
        fields = ["text"]

