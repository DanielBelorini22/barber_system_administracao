from django.forms.widgets import PasswordInput
from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password')
        widgets = {
            'password': PasswordInput(),
        }
