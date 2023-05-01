from django.urls import path
from . import views
# from .admin import asset_management_admin_site
from django.contrib import admin
# admin.site.site_header = "Administration"
urlpatterns = [
    path('',views.Index,name='home'),
    # path('asset-management/', asset_management_admin_site.urls),
    path('test/',views.check,name='check')
]
