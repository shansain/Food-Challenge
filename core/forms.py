import datetime
from django import forms
from django.utils import timezone


class SignUpForm(forms.Form):
    username = forms.CharField(
        label='User name',
        max_length=200, widget=forms.TextInput(attrs={'class': 'from-control'}))
    email = forms.EmailField(label='Email', max_length=200)
    password = forms.CharField(label='Password', max_length=200, widget=forms.PasswordInput)