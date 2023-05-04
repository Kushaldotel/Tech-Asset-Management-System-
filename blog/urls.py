from django.urls import path
from . import views
# from .admin import asset_management_admin_site
from django.contrib import admin
from django.shortcuts import redirect
# admin.site.site_header = "Administration"

urlpatterns = [
    path('', lambda request: redirect('/admin/')),
    # path('',views.Index,name='home'),
    # path('asset-management/', asset_management_admin_site.urls),
    # path('test/',views.check,name='check'),
    #path('admin/',views.Admin,name='check-admin')
    
]
