import string
from django.db import models
import random
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

# Create your models here.



class Vendor(models.Model):
    CITIZENSHIP = 'citizenship'
    PASSPORT = 'passport'
    VOTER_ID = 'voter_id'
    ID_CHOICES = [
        (CITIZENSHIP, 'Citizenship'),
        (PASSPORT, 'Passport'),
        (VOTER_ID, 'Voter ID'),
    ]
    
    full_name = models.CharField(max_length=255, help_text='Enter the name of vendor', verbose_name='Full Name')
    vat_pan = models.CharField(max_length=50, verbose_name='VAT/PAN')
    address = models.CharField(max_length=255, verbose_name='Address')
    phone = models.CharField(max_length=20, verbose_name='Phone',null=True)
    email = models.EmailField(verbose_name='Email',null=True)
    
    contact_person = models.CharField(max_length=255,null=True, blank=True, verbose_name='Contact Person')
    
    document_link = models.URLField(max_length=255,null=True,  blank=True, verbose_name='Document Link')
    description = models.TextField(null=True, blank=True, verbose_name='Description')
    owner_name = models.CharField(max_length=255, verbose_name='Owner Name',null=True,blank=True)
    
    owner_id_type = models.CharField(max_length=20, choices=ID_CHOICES, verbose_name='Owner ID Type',null=True,blank=True)
    owner_id_file = models.ImageField(upload_to='vendor_proofs/', null=True, blank=True, verbose_name='Owner ID File')
    owner_email = models.EmailField(verbose_name='Owner Email',null=True,blank=True)
    owner_phone = models.CharField(max_length=20, verbose_name='Owner Phone',null=True,blank=True)
    owner_address = models.CharField(max_length=255, verbose_name='Owner Address',null=True,blank=True)

    def __str__(self):
        return self.full_name

      
class SoftwareType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    vendor = models.ForeignKey(Vendor,on_delete=models.SET_NULL,blank=True,null=True)
    def __str__(self):
        return self.name

class Criticality(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    


class Country(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = _('Countries')
    
class State(models.Model):
    name = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    
class BranchStatus(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
   

class ManagedBy(models.Model):
    name = models.CharField(max_length=255,verbose_name='Department Name')
    code = models.CharField(max_length=20,null=True,verbose_name='Dept_Code')
    description = models.TextField(null=True,blank=True)
    # addtobranch = models.ManyToManyField('Branch', blank=True)
    def __str__(self):
        return self.name    

    # def save(self, *args, **kwargs):
    #     super(ManagedBy, self).save(*args, **kwargs)
    #     department_name = self.name
    #     for branch in self.addtobranch.all():
    #         branch.departments.add(department_name)
    #         branch.save()
            
    class Meta:
        verbose_name_plural = _('Departments')


class Branch(models.Model):
    branch_name = models.CharField(max_length=100)
    branch_code = models.CharField(max_length=50, unique=True)
    branch_incharge_name = models.CharField(max_length=100)
    branch_incharge_phone = models.CharField(max_length=15)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    city = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)
    email = models.EmailField(max_length=254)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    fax = models.CharField(max_length=15, blank=True)
    established_year = models.PositiveIntegerField()
    website = models.URLField(blank=True)
    status = models.ForeignKey(BranchStatus, on_delete=models.CASCADE)
    departments = models.ManyToManyField(ManagedBy)

    class Meta:
        verbose_name_plural = _('Branches')
        # you will find the model branch with name Branches with this class

    def __str__(self):
        return self.branch_name


    
class Software(models.Model):
    name = models.CharField(max_length=255)
    software_type = models.ForeignKey(SoftwareType, on_delete=models.CASCADE)
    criticality = models.ForeignKey(Criticality, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor,on_delete=models.SET_NULL,blank=True,null=True)
    managed_by = models.ForeignKey(ManagedBy, on_delete=models.CASCADE)
    purchase_price = models.PositiveIntegerField(null=True, blank=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL,null=True,blank=True)
    is_deleted = models.BooleanField(default=False)
    
    
    # def __str__(self):
    #     return f"The software {self.name} is managed by {self.managed_by} as the criticality is {self.criticality}"
    
    
class DocumentCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=200)
    def __str__(self):
        return self.name

class Document(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(DocumentCategory, on_delete=models.CASCADE)
    criticality = models.ForeignKey(Criticality, on_delete=models.CASCADE)
    managed_by = models.ForeignKey(ManagedBy, on_delete=models.CASCADE)
    file = models.FileField(upload_to='document/')
    # you can change this upload to section as you need. It will open a new folder in media root and save there

    def __str__(self):
        return self.name
    
# class Document_Type(models.Model):
#     name = models.CharField(max_length=100)
#     def __str__(self):
#         return self.name

class Status(models.Model):
    name = models.CharField(max_length=100)
    deleted = models.DateTimeField(null=True, blank=True)
    def __str__(self):     
        return self.name


class Service_Category(models.Model):
    name = models.CharField(max_length=100)
    vendor = models.ForeignKey(Vendor,on_delete=models.SET_NULL,blank=True,null=True)
    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=100)
    service_type = models.ForeignKey(Service_Category,on_delete=models.CASCADE)
    criticality = models.ForeignKey(Criticality, on_delete=models.CASCADE)
    managed_by = models.ForeignKey(ManagedBy, on_delete=models.CASCADE) 
    document = models.ForeignKey(Document,on_delete=models.CASCADE)
    purchase_price = models.PositiveIntegerField(null=True, blank=True)
    purchase_date = models.DateField()
    expiry_date = models.DateField()
    status = models.ForeignKey(Status,on_delete=models.CASCADE)
    service_tag = models.CharField(max_length=8, unique=True,editable=False)
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.service_tag:
            self.service_tag = ''.join(random.choices(string.digits, k=8))
        super().save(*args, **kwargs)

class Insurance(models.Model):
    POLICY_NUMBER_MAX_LENGTH = 100
    COMPANY_NAME_MAX_LENGTH = 100
    INSURANCE_AMOUNT_MAX_DIGITS = 15
    INSURANCE_AMOUNT_DECIMAL_PLACES = 2
    PREMIUM_PRICE_MAX_DIGITS = 15
    PREMIUM_PRICE_DECIMAL_PLACES = 2
    MATURITY_TIME_CHOICES = [
        ('1', '1 month'),
        ('3', '3 months'),
        ('6', '6 months'),
        ('12', '12 months'),
    ]
    PAYMENT_TIME_CHOICES = [
        ('Monthly', 'Monthly'),
        ('Quarterly', 'Quarterly'),
        ('Half-Yearly', 'Half-Yearly'),
        ('Yearly', 'Yearly'),
    ]
  
    policy_number = models.CharField(max_length=POLICY_NUMBER_MAX_LENGTH)
    company_name = models.CharField(max_length=COMPANY_NAME_MAX_LENGTH)
    insurance_amount = models.DecimalField(max_digits=INSURANCE_AMOUNT_MAX_DIGITS, decimal_places=INSURANCE_AMOUNT_DECIMAL_PLACES)
    premium_price = models.DecimalField(max_digits=PREMIUM_PRICE_MAX_DIGITS, decimal_places=PREMIUM_PRICE_DECIMAL_PLACES)
    insurance_date = models.DateField()
    maturity_time = models.CharField(max_length=2, choices=MATURITY_TIME_CHOICES)
    payment_time = models.CharField(max_length=20, choices=PAYMENT_TIME_CHOICES)
    
    def __str__(self):
        return self.policy_number



class HardwareType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name

class Hardware(models.Model):
    name = models.CharField(max_length=100)
    hardware_type = models.ForeignKey(HardwareType,on_delete=models.SET_NULL,null=True)
    vendor = models.ForeignKey(Vendor,on_delete=models.SET_NULL,blank=True,null=True)
    criticality = models.ForeignKey(Criticality, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch,on_delete=models.SET_NULL,blank=True,null=True)
    managed_by = models.ForeignKey(ManagedBy, on_delete=models.CASCADE) 
    document = models.ForeignKey(Document,on_delete=models.CASCADE)
    status = models.ForeignKey(Status,on_delete=models.CASCADE)
    purchase_date = models.DateField()
    expiry_date = models.DateField()  
    billing_no = models.PositiveIntegerField()
    serial_no = models.PositiveIntegerField()
    purchase_price = models.PositiveIntegerField()
    insurance = models.ForeignKey(Insurance,on_delete=models.SET_NULL,blank=True,null=True)
    
    def __str__(self):
        return self.name
    
class Organization_Details(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50)
    established_year = models.PositiveIntegerField()
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    fax = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    website = models.URLField(max_length=200)
    logo = models.ImageField(upload_to='organization_logos/', null=True, blank=True)
    branches = models.ManyToManyField(Branch, related_name='organizations', blank=True)
    def __str__(self):
        return self.name
    
    # def save(self, *args, **kwargs):
    #     # Override the save method to ensure only one instance exists
    #     if Country.objects.exists() and not self.pk:
    #         # If an instance already exists, prevent creating a new one
    #         raise ValidationError('Only one instance of Country can be created')
    #     return super().save(*args, **kwargs)


class Issue_Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name


class Issue(models.Model):
    ASSET_CATEGORY_CHOICES = [
        ('hardware', 'Hardware'),
        ('software', 'Software'),
        ('document', 'Document'),
        ('service', 'Service'),
    ]
    Issue_Status_CHOICES = [
        ('open', 'Open'),
        ('closed', 'Closed'),
        ('pending', 'Pending'),
        ('resolved', 'Resolved'),
    ]
    asset_category = models.CharField(max_length=20, choices=ASSET_CATEGORY_CHOICES)
    title = models.CharField(max_length=100)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Issue_Category, on_delete=models.SET_NULL, null=True)
    asset_name = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=Issue_Status_CHOICES, default='open')

    def __str__(self):
        return self.title


class AssetRequest(models.Model):
    ASSET_TYPES = [
        ('Hardware', 'Hardware'),
        ('Service', 'Service'),
        ('Software', 'Software'),
        ('Document', 'Document'),
    ]

    PRIORITIES = [
        ('Uregent', 'Uregent'),
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('low', 'low'),
    ]
    PRIORITIES2 = [
        ('Request', 'Request'),
        ('Approve', 'Approve'),
        ('Cancel', 'Cancel'),
    ]

    asset_type = models.CharField(choices=ASSET_TYPES, max_length=10)
    asset_name = models.CharField(max_length=255)
    tentative_cost = models.DecimalField(max_digits=10, decimal_places=2)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)  # Foreign key to Branch model
    department = models.ForeignKey(ManagedBy, on_delete=models.CASCADE)  # Foreign key to Department model
    description = models.TextField()
    priority = models.CharField(choices=PRIORITIES, max_length=10)
    status = models.CharField(choices=PRIORITIES2,max_length=255)


class Asset(models.Model):
    hardware_name = models.CharField(max_length=255)
    dashboard_value = models.BooleanField(default=True)
    software_value = models.BooleanField(default=True)
    def __str__(self):
        return self.hardware_name




