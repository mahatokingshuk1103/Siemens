
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ('location','temperature','humidity')  # Customize displayed fields
    

admin.site.register(Item, ItemAdmin)  # Register with custom admin class


