from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class Banks(models.Model):
    name=models.CharField(max_length=49)
    id=models.PositiveIntegerField(primary_key=True)

class Branches(models.Model):
    ifsc=models.CharField(max_length=11, primary_key=True)
    bank=models.ForeignKey(Banks,on_delete=models.CASCADE)
    branch=models.CharField(max_length=74)
    address=models.CharField(max_length=195)
    city=models.CharField(max_length=50)
    district=models.CharField(max_length=50)
    state=models.CharField(max_length=26)

class User(AbstractUser):
    username=models.CharField(max_length=50, unique=True)
    email=models.EmailField(('email address'),unique=True)
    USERNAME_FIELD='username'
    REQUIRED_FIELDS=['email','first_name','last_name']

    def __str__(self):
        return "{}".format(self.email)