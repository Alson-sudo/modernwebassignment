from django import forms
from .models import Profiles
from django.forms import ModelForm


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ProfilesForm(ModelForm):
    class Meta:
        model = Profiles
        fields = '__all__'
        exclude = ['user']




