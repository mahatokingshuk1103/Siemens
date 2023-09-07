from django.db import models

# Create your models here.
class ExcelData(models.Model):
    timestamp = models.DateTimeField()
    country_name = models.CharField(max_length=50)
    name = models.CharField(max_length=20)
    capacity_mw = models.FloatField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    primary_fuel = models.CharField(max_length=20)


    def __str__(self):
        return f"{self.timestamp} - {self.country_name} - {self.name} - {self.capacity_mw} - {self.latitude} - {self.longitude} - {self.primary_fuel}"

