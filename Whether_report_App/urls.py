from django.urls import path
from . import views

urlpatterns = [
    path('weather/', views.weather_data_view, name='weather-data'),
]
