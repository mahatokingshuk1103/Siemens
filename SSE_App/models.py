from django.db import models

class SSEDataPoint(models.Model):
     time = models.TimeField(auto_now_add=True)
     humidity = models.DecimalField(max_digits=5, decimal_places=2)
     temperature = models.DecimalField(max_digits=5, decimal_places=2)


# Create your models here.
