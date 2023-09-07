from rest_framework import serializers
from .models import IoTData

class IoTDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = IoTData
        fields = ('device_id', 'temperature', 'humidity')
