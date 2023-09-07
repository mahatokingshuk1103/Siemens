from django.contrib import admin
# excel_import/admin.py
from django.contrib import admin
from .models import ExcelData  # Import your model here

admin.site.register(ExcelData)


# Register your models here.
