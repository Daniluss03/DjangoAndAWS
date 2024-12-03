from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    profile_picture=models.ImageField( null=True,blank=True,default='Default.png')
    user=models.ForeignKey(User,max_length=10,on_delete=models.CASCADE,null=True)

class UserRegistration():
    pass