from django.contrib import admin
from .models import Store
from inventories.models import Inventory

# Register your models here.
admin.site.register(Store)
admin.site.register(Inventory)