from django.db import models

# Create your models here.

class Friend(models.Model):
    name = models.CharField(max_length=100)           #user name
    dob = models.CharField(max_length=100)            #date of birth
    address = models.CharField(max_length=100)        #user address
    description = models.CharField(max_length=100)    #user description
    createdAt = models.CharField(max_length=100)      #user createdAt


