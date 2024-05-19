from django import forms
from .models import UserData

class RegisterForm(forms.Form):
    f_name = forms.CharField(max_length=50)
    l_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)
    rut = forms.CharField(max_length=9)
    address = forms.CharField(max_length=200)
    phone = forms.CharField(max_length=12)

    def clean_rut(self):
        rut = self.cleaned_data['rut']
        rut = rut.replace('.', '').replace(',', '').replace('-', '')
        if UserData.objects.filter(rut=rut).exists():
            raise forms.ValidationError('Ya existe un usuario con este RUT.')
        return rut