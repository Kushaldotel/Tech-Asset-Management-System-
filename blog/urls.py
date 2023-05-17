from django.urls import path
from . import views
# from .admin import asset_management_admin_site
from django.contrib import admin
from django.shortcuts import redirect
from django.contrib.auth.views import logout_then_login

# admin.site.site_header = "Administration"

urlpatterns = [
    path('', lambda request: redirect('/dashboard/')), # this to go to the admin link directly
    path('',views.Home,name='home'),
    # path('asset-management/', asset_management_admin_site.urls),
    # path('test/',views.check,name='check'),
    #path('admin/',views.Admin,name='check-admin'),
    path('check/',views.check,name='check'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('logout/', logout_then_login, name='logout_then_login'),
    
    # path('hardware_list/',views.hardware_list,name='hardware_list'),
    # path('add_hardware/',views.add_hardware,name='add_hardware'),
    #  path('delete_hardware/', views.delete_hardware, name='delete_hardware'),
    #  path('edit_hardware/<int:hardware_id>/', views.edit_hardware, name='edit_hardware'),
    
    
     path('organization/edit/', views.edit_organization, name='edit_organization'),
    #  path('state/', views.state_list, name='state'),
     path('add_state/', views.add_state, name='add_state'),
     path('trash-state/', views.trash_state, name='trash_state'),
     path('state/', views.state_list, name='state'),
     
     path('delete/',views.delete_state,name='delete'),
     path('restore_state/',views.restore_state,name='restore'),
     path('delete_state_permanently/',views.delete_state_permanently,name='permanent'),
     
     path('issue_list/',views.issue_list,name='issue_list'), 
     path('issue/',views.create_issue,name='issue'),
     path('issue/<int:pk>/', views.issue_detail, name='issue_detail'),
     path('create_issue_category/',views.create_issue_category,name='create_issue_category'),
     path('issue_category/',views.issue_Category_list, name='issue_category'),
     
     path('asset-requests/', views.asset_request_list, name='asset_request_list'),
     path('add_asset_request/', views.add_asset_request, name='add_asset_request'),
     path('asset-requests/<int:pk>/', views.asset_request_edit, name='asset_request_edit'),
     
     path('software_type/',views.software_type_list, name='software_types'),
     path('add_software_type/',views.create_software_type, name='add_software_type'),
     path('software-type/edit/<int:software_type_id>/', views.edit_software_type, name='edit_software_type'),
    #  path('delete-state-permanently/', views.delete_state_permanently, name='delete_state_permanently'),
    
    
    path('service_type/',views.service_type_list, name='service_types'),
     path('add_service_type/',views.create_service_type, name='add_service_type'),
     path('service-type/edit/<int:service_type_id>/', views.edit_service_type, name='edit_service_type'),
     
     
     path('document_type/',views.document_type_list, name='document_types'),
     path('add_document_type/',views.create_document_type, name='add_document_type'),
     path('document-type/edit/<int:document_type_id>/', views.edit_document_type, name='edit_document_type'),
     
     
    path('branches/', views.BranchListView.as_view(), name='branch_list'),
    path('branches/add/', views.AddBranchView.as_view(), name='add_branch'),
    path('branches/edit/<int:branch_id>/', views.EditBranchView.as_view(), name='edit_branch'),
    
    path('departments/', views.department_list, name='department_list'),
    path('departments/add/', views.add_department, name='add_department'),
    path('departments/<int:department_id>/edit/', views.edit_department, name='edit_department'),
     
     
    path('vendors/', views.VendorListView.as_view(), name='vendor_list'),
    path('vendors/add/', views.AddVendorView.as_view(), name='add_vendor'),
    path('vendors/edit/<int:vendor_id>/', views.EditVendorView.as_view(), name='edit_vendor'),
    
    
    path('hardware/', views.hardware_list, name='hardware_list'),
    path('hardware/add/', views.add_hardware, name='add_hardware'),
    path('hardware/edit/<int:hardware_id>/', views.edit_hardware, name='edit_hardware'),
    
    path('software/', views.software_list, name='software_list'),
    path('software/add/', views.add_software, name='add_software'),
    path('software/edit/<int:software_id>/', views.edit_software, name='edit_software'),
    
    
    path('documents/', views.document_list, name='document_list'),
    path('documents/add/', views.add_document, name='add_document'),
    path('documents/edit/<int:document_id>/', views.edit_document, name='edit_document'),
    
    
    path('services/', views.service_list, name='service_list'),
    path('add_service/', views.add_service, name='add_service'),
    path('service/edit/<int:service_id>/', views.edit_service, name='edit_service'),
]
