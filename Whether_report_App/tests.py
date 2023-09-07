from django.test import TestCase
from django.db import models

class APIData(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# Create your tests here.
