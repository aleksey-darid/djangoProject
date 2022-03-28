
from django import forms

from Users.models import WorkersModel


class WorkersForm(forms.ModelForm):
    class Meta:
        model = WorkersModel
        fields = ["rate_per_hour"]