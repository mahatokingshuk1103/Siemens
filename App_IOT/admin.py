from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import IoTData

class IoTDataAdmin(admin.ModelAdmin):
    list_display = ('device_id', 'timestamp', 'temperature','humidity')  # Customize displayed fields
    

admin.site.register(IoTData, IoTDataAdmin)  # Register with custom admin class


