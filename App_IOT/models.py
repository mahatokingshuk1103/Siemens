from django.db import models

class IoTData(models.Model):
    device_id = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    humidity = models.FloatField()

    def __str__(self):
        return f"Device {self.device_id} - {self.timestamp}"
