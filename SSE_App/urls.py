from django.urls import path
from . import views

urlpatterns = [
    path('sse/', views.sse, name='sse'),
]
