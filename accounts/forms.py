from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class sigup(UserCreationForm):
    email =forms.CharField(max_length=100,required=True,widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ['username','email','password1','password2']