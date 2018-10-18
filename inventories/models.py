from django.db import models
from django.contrib.auth.models import User
from stores.models import Store
# Create your models here.


class Inventory(models.Model):
    store = models.ForeignKey(Store, default=1, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    is_empty = models.BooleanField()
    last_updated = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.name