from django.forms import ModelForm, Select
from django import forms
from users.models import Comuna 

from .models import Property, Request, Contract

class PropertyForm(ModelForm):
    comuna = forms.ModelChoiceField(queryset=Comuna.objects.all(), widget=forms.Select)

    class Meta:
        model = Property
        fields = '__all__'
        widgets = {
            'comuna': Select()
        }

class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields = '__all__'

class ContractForm(ModelForm):
    class Meta:
        model = Contract
        fields = '__all__'