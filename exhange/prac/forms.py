from django import forms
from django.conf import settings
from .models import trade
class trade_form(forms.ModelForm):
    class Meta:
        model=trade
        fields = "__all__"
    