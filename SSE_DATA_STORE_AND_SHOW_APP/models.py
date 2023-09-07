from django.db import models

# Create your models here.
from django.db import models

class SSEDATAPOINT(models.Model):
    
    time = models.DateTimeField()
    humidity = models.FloatField()
    temperature = models.FloatField()



# Create your models here.

