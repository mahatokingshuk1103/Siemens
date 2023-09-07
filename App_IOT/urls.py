from django.urls import include, path
from .views import IoTDataView

urlpatterns = [
    path('iotdata/', IoTDataView.as_view(), name='iot-data'),
    path('IOT',include('IOT_upload_App')),
]
