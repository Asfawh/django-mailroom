# Create models here.
# mailroomapp/models.py
from django.db import models
from django import forms

class User(models.Model):
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
#     password = forms.CharField(widget=forms.PasswordInput())

class Donor(models.Model):
    name = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.name

class Donations(models.Model):
    value = models.IntegerField()
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    def __str__(self):
        return self.value
