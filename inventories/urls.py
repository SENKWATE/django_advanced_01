from django.urls import path
from inventories import views

# equivelent to name = 'inventories-list'
app_name = 'inventories' 

urlpatterns = [
    path('inventory_list/', views.inventory_list, name="list"),
   
]