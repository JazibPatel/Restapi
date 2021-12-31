from django.db import models

# Create your models here.

class Employee(models.Model):
    employid = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
