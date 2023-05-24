from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Software)
admin.site.register(SoftwareType)