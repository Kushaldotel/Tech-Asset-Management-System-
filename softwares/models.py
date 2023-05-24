from django.db import models

# Create your models here.

class SoftwareType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    # vendor = models.ForeignKey(Vendor,on_delete=models.SET_NULL,blank=True,null=True)
    def __str__(self):
        return self.name


class Software(models.Model):
    name = models.CharField(max_length=255)
    software_type = models.ForeignKey(SoftwareType, on_delete=models.CASCADE)
    # criticality = models.ForeignKey(Criticality, on_delete=models.CASCADE)
    # vendor = models.ForeignKey(Vendor,on_delete=models.SET_NULL,blank=True,null=True)
    # managed_by = models.ForeignKey(ManagedBy, on_delete=models.CASCADE)
    purchase_price = models.PositiveIntegerField(null=True, blank=True)
    # branch = models.ForeignKey(Branch, on_delete=models.SET_NULL,null=True,blank=True)
    
    def __str__(self):
        return self.name