from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Cost


User = get_user_model()


class CostForm(ModelForm):
    class Meta:
        model = Cost
        fields = ['amount','transaction_type','name']


class CostForm(forms.ModelForm):
    class Meta:
        model = Cost
        fields = ['name', 'amount', 'transaction_type']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'transaction_type': forms.Select(attrs={'class': 'form-control'}),
        }