from django.db import models

# Create your models here.
from django.db import models

class Device(models.Model):
    name = models.CharField(max_length=100)
    mac_address = models.CharField(max_length=17)
    
    def __str__(self):
        return self.name
