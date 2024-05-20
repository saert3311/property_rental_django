from django import forms
from .models import UserData

class RegisterForm(forms.Form):
    f_name = forms.CharField(max_length=50)
    l_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    username = forms.CharField(max_length=20)
    password_repeat = forms.CharField(widget=forms.PasswordInput)
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
    
    def clean_password(self):
        password = self.cleaned_data['password']
        print(self.cleaned_data)
        password_repeat = self.cleaned_data['password_repeat']
        if len(password) < 8:
            raise forms.ValidationError('La contraseña debe tener al menos 8 caracteres.')
        if password != password_repeat:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return password