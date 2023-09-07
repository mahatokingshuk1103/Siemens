"""
URL configuration for Python_ETL_IOT project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from App_IOT.views import IoTDataView,data_list_view
from Excell_Upload_App.views import upload_excel,display_data
from Whether_report_App.views import weather_view
from QRScanner_App.views import generate_qr_code,add_item
from SSE_DATA_STORE_AND_SHOW_APP.views import save_data_to_database,show_data,chart_view
from SSE_DATA_GENERATOR_APP.views import sse


urlpatterns = [
    path('admin/', admin.site.urls),
    path('iotdata/', IoTDataView.as_view(), name='iot-data'),
    path('data/' ,data_list_view),
    path('upload_excel/', upload_excel, name='upload_excel'),
    path('display/', display_data, name='display_data'),
    
    path('weather/', weather_view, name='weather'),
    path('generate_qr/<int:item_id>/', generate_qr_code, name='generate_qr_code'),
    path('upload_qr/',add_item,name='add_item'),
    path('save/', save_data_to_database, name='save_data_to_database'),
    path('sse/', sse , name='sse'),
    path('show/',show_data , name='show_data'),
    path('chart/', chart_view, name='chart')
    

]
