import random
import string
from django.contrib import admin
from .models import Criticality,ManagedBy,Software,SoftwareType,Vendor
from .models import Document,DocumentCategory,Status,Service,HardwareType,Hardware
from .models import Insurance,Country,State,BranchStatus,Branch,Organization_Details


class DocumentAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'criticality', 'managed_by', 'file')
    list_filter = ('name', 'category', 'criticality', 'managed_by', 'file')

    fields = ('name', 'category', 'criticality', 'managed_by', 'file')
    search_fields = ['__all__'] 
    

# Register your models here.
class SoftwareAdmin(admin.ModelAdmin):
    list_display = ('name', 'software_type', 'criticality', 'vendor', 'managed_by')

    list_filter = ('software_type', 'criticality', 'vendor', 'managed_by')
    search_fields = ['__all__'] 


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'criticality', 'managed_by', 'document', 'purchase_date', 'expiry_date','status', 'service_tag')    
    readonly_fields = ('service_tag',)
    search_fields = ['__all__'] 
    
    # def save_model(self, request, obj, form, change):
    #     if not obj.service_tag:
    #         obj.service_tag = ''.join(random.choices(string.digits, k=8))
    #     super().save_model(request, obj, form, change)

class HardwareAdmin(admin.ModelAdmin):
    list_display = ('name', 'hardware_type', 'insurance','vendor', 'criticality','branch','managed_by', 'document', 'status', 'purchase_date', 'expiry_date', 'billing_no', 'serial_no', 'purchase_price')
    search_fields = ['__all__'] 
    list_filter = ('hardware_type', 'vendor', 'criticality', 'managed_by', 'status')
    
class InsuranceAdmin(admin.ModelAdmin):
    list_display = ('policy_number', 'company_name', 'insurance_amount', 'premium_price', 'insurance_date', 'maturity_time', 'payment_time')
 

class BranchAdmin(admin.ModelAdmin):
    list_display = ('branch_name', 'branch_code', 'branch_incharge_name', 'branch_incharge_phone')
    def get_departments(self, obj):
        return ", ".join([str(department) for department in obj.departments.all()])

    get_departments.short_description = 'Departments'

class Organization_DetailsAdmin(admin.ModelAdmin):
    # list_display = ('name', 'established_year', 'country', 'state', 'city', 'phone', 'email','display_branches')
    list_display = ('name', 'established_year', 'country', 'state', 'city', 'phone', 'email')
    def has_add_permission(self, request):
        if Organization_Details.objects.exists():
            return False
        else:
            return True

class VendorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'vat_pan', 'address', 'phone', 'email')
    list_filter = ('full_name','phone')
    
class ManagedByAdmin(admin.ModelAdmin):
    list_display = ('name','code')

# class AssetManagementAdminSite(admin.AdminSite):
#     site_header = 'Asset Management'

# asset_management_admin_site = AssetManagementAdminSite(name='asset_management_admin')

# asset_management_admin_site.register(Software,SoftwareAdmin)
# asset_management_admin_site.register(Hardware,HardwareAdmin)
# asset_management_admin_site.register(Document,DocumentAdmin)
# asset_management_admin_site.register(Service,ServiceAdmin)


admin.site.register(Branch, BranchAdmin)

admin.site.register(Insurance, InsuranceAdmin) 
   
admin.site.register(Software,SoftwareAdmin)

admin.site.register(Document, DocumentAdmin)

admin.site.register(Service,ServiceAdmin)

admin.site.register(Hardware,HardwareAdmin)



admin.site.register(Organization_Details, Organization_DetailsAdmin)

admin.site.register(Vendor,VendorAdmin)


admin.site.register(DocumentCategory)
admin.site.register(Criticality)
admin.site.register(ManagedBy,ManagedByAdmin)
admin.site.register(SoftwareType)
admin.site.register(HardwareType)


# admin.site.register(Document_Type)
admin.site.register(Status)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(BranchStatus)

#Model of another app
# admin.site.register(Check)

