from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
#User login

from  django.contrib.auth.forms import AuthenticationForm  

from django.forms.widgets import PasswordInput,TextInput

from django import forms

class UserForm(UserCreationForm):
    class  Meta:
        model=User
        fields={'username','email','password1','password2'}
       


class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=TextInput()) 
    password=forms.CharField(widget=PasswordInput())