
#user Registration

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

from . models import Profile

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


#Profile manage,ent -Update
class UpdateUserForm(forms.ModelForm):
    password=None
    class Meta:
        model=User
        fields=['username','email']
        exclude=['password1','password2',]


class updatePicture(forms.ModelForm):
    profile_picture=forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control-file'}))
    class Meta:
        model=Profile
        fields=['profile_picture']