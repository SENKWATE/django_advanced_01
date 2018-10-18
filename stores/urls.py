from django.contrib import admin
from django.urls import path, include
from stores.views import store_list

app_name = 'stores'

urlpatterns = [
    path('list/', store_list, name='list'),
]
