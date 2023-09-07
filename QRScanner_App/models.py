from django.db import models
# models.py
from django.db import models

class Item(models.Model):
    location = models.CharField(max_length=100)
    temperature = models.FloatField(default='0.0')
    humidity = models.FloatField(default='0.0')

    def __str__(self):
        return f"Device {self.location} - {self.temperature}"
