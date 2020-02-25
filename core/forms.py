import datetime
from django import forms
from django.utils import timezone

# class SignUpForm(forms.Form):
#     username = forms.CharField(
#         label='User name',
#         max_length=200, widget=forms.TextInput(attrs={'class': 'from-control'}))
#     email = forms.EmailField(label='Email', max_length=200)
#     password = forms.CharField(label='Password', max_length=200, widget=forms.PasswordInput)
from core.models import Business


class SignUpBusinessForm(forms.ModelForm):
    username = forms.CharField(
        label='User name',
        max_length=200, widget=forms.TextInput(attrs={'class': 'from-control'}))
    first_name = forms.CharField(label='first_name', max_length=100)
    email = forms.EmailField(label='Email', max_length=200)
    password = forms.CharField(label='Password', max_length=200, widget=forms.PasswordInput)

    class Meta:
        model = Business
        fields = ['username', 'location', 'description', 'email', 'password',
                  'days', 'start_hour', 'end_hour']
        widgets = {
            'start_hour': forms.Select(
                attrs={'class': 'from-control'},
                choices=((f'{x}:00', f'{x}:00') for x in range(6, 24))),
            'end_hour': forms.Select(choices=((f'{x}:00', f'{x}:00') for x in range(6, 24)))
        }


class SignUpClientForm(forms.Form):
    username = forms.CharField(
        label='User name',
        max_length=200, widget=forms.TextInput(attrs={'class': 'from-control'}))

    email = forms.EmailField(label='Email', max_length=200)
    password = forms.CharField(label='Password', max_length=200, widget=forms.PasswordInput)
