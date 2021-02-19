from django.utils import timezone
from django.db import models

# Create your models here.

class VerificationInfo(models.Model):
    propOwnerFullName = models.CharField(max_length=50,default='null')
    propOwnerContact = models.CharField(max_length=30,default='null')
    propOwnerEmail = models.EmailField(default='null')
    propOwnerFlatno = models.CharField(max_length=50,default='null')
    propOwnerAddress = models.CharField(max_length=50,default='null')
    propOwnerCity = models.CharField(max_length=50,default='null')
    propOwnerState = models.CharField(max_length=50,default='null')
    propOwnerCountry = models.CharField(max_length=50,default='null')
    tenantFullName = models.CharField(max_length=50,default='null')
    tenantContact = models.CharField(max_length=30,default='null')
    tenantEmail = models.EmailField(default='null')
    tenantFlatno = models.CharField(max_length=50,default='null')
    tenantAddress = models.CharField(max_length=50,default='null')
    tenantCity = models.CharField(max_length=50,default='null')
    tenantState = models.CharField(max_length=50,default='null')
    tenantCountry = models.CharField(max_length=50,default='null')
    tenantDOB = models.DateField(blank=True,null=True,default=timezone.now)
    tenantReason = models.TextField(default='null')
    tenantOrganisation = models.CharField(max_length=50,default="Not Applicable")
    tenantDepartment =models.CharField(max_length=50, default="Not Applicable")
    tenantID = models.CharField(max_length=50, default="Not Applicable")
    tenantInstitute = models.CharField(max_length=50 , default="Not Applicable")
    tenantBranch = models.CharField(max_length=50, default="Not Applicable")
    desc = models.TextField(default="Not Applicable")

    def __str__(self):
        return self.propOwnerFullName
