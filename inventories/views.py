from django.shortcuts import render
from stores.models import Store
from inventories.models import Inventory
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
    CreateAPIView,
)

def inventory_list(request):
    context = {
        "inventories": Inventory.objects.all()
    }
    return render(request, 'inventory_list.html', context)

