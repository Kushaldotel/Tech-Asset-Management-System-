from django.urls import path
from . import views
# from .admin import asset_management_admin_site
from django.contrib import admin
from django.shortcuts import redirect
from django.contrib.auth.views import logout_then_login

# admin.site.site_header = "Administration"

urlpatterns = [
    # path('', lambda request: redirect('/admin/')), this to go to the admin link directly
    path('',views.Home,name='home'),
    # path('asset-management/', asset_management_admin_site.urls),
    # path('test/',views.check,name='check'),
    #path('admin/',views.Admin,name='check-admin'),
    path('check/',views.check,name='check'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('logout/', logout_then_login, name='logout_then_login'),
    path('hardware_list/',views.hardware_list,name='hardware_list'),
    path('add_hardware/',views.add_hardware,name='add_hardware'),
     path('delete_hardware/', views.delete_hardware, name='delete_hardware'),
     path('edit_hardware/<int:hardware_id>/', views.edit_hardware, name='edit_hardware'),
     path('organization/edit/', views.edit_organization, name='edit_organization'),

]
