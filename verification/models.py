from django.utils import timezone
from django.db import models

# Create your models here.

class VerificationInfo(models.Model):
    propOwnerFullName = models.CharField(max_length=50,default='-')
    propOwnerContact = models.CharField(max_length=30,default='-')
    propOwnerEmail = models.EmailField(default='-')
    propOwnerFlatno = models.CharField(max_length=50,default='-')
    propOwnerAddress = models.CharField(max_length=50,default='-')
    propOwnerCity = models.CharField(max_length=50,default='-')
    propOwnerState = models.CharField(max_length=50,default='-')
    propOwnerCountry = models.CharField(max_length=50,default='-')
    tenantFullName = models.CharField(max_length=50,default='-')
    tenantContact = models.CharField(max_length=30,default='-')
    tenantEmail = models.EmailField(default='-')
    tenantFlatno = models.CharField(max_length=50,default='-')
    tenantAddress = models.CharField(max_length=50,default='-')
    tenantCity = models.CharField(max_length=50,default='-')
    tenantState = models.CharField(max_length=50,default='-')
    tenantCountry = models.CharField(max_length=50,default='-')
    tenantDOB = models.DateField(blank=True,null=True,default=timezone.now)
    tenantReason = models.CharField(max_length=250,default='-')
    tenantOrganisation = models.CharField(max_length=50,default="N.A.")
    tenantDepartment =models.CharField(max_length=50, default="N.A")
    tenantID = models.CharField(max_length=50, default="N.A.")
    tenantInstitute = models.CharField(max_length=50 , default="N.A.")
    tenantBranch = models.CharField(max_length=50, default="N.A.")
    desc = models.CharField(max_length=250,default="N.A.")

    def __str__(self):
        return self.tenantFullName

