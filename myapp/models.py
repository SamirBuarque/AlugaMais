from django.db import models

# Create your models here.

class test(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField(max_length=100)
    birth = models.DateField