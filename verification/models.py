from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models

# Create your models here.

class VerificationInfo(models.Model):
    admin_status = (
        ('under scrutiny','Under Scrutiny'),
        ('approved','Approved'),
        ('rejected','Rejected')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    propOwnerFullName = models.CharField(max_length=50,blank=True)
    propOwnerContact = models.CharField(max_length=30,blank=True)
    propOwnerEmail = models.EmailField(blank=True)
    propOwnerFlatno = models.CharField(max_length=50,blank=True)
    propOwnerAddress = models.CharField(max_length=50,blank=True)
    propOwnerCity = models.CharField(max_length=50,blank=True)
    propOwnerState = models.CharField(max_length=50,blank=True)
    propOwnerCountry = models.CharField(max_length=50,blank=True)
    tenantFullName = models.CharField(max_length=50,blank=True)
    tenantContact = models.CharField(max_length=30,blank=True)
    tenantEmail = models.EmailField(blank=True)
    tenantFlatno = models.CharField(max_length=50,blank=True)
    tenantAddress = models.CharField(max_length=50,blank=True)
    tenantCity = models.CharField(max_length=50,blank=True)
    tenantState = models.CharField(max_length=50,blank=True)
    tenantCountry = models.CharField(max_length=50,blank=True)
    tenantDOB = models.DateField(blank=True,null=True,default=timezone.now)
    tenantReason = models.CharField(max_length=250,blank=True)
    tenantOrganisation = models.CharField(max_length=50,blank=True)
    tenantDepartment =models.CharField(max_length=50, blank=True)
    tenantID = models.CharField(max_length=50, blank=True)
    tenantInstitute = models.CharField(max_length=50 ,blank=True)
    tenantBranch = models.CharField(max_length=50, blank=True)
    desc = models.CharField(max_length=250,blank=True)
    admin_status = models.CharField(max_length=30,choices=admin_status,default='under scrutiny')
    admin_message = models.CharField(max_length=250,default="Your complaint is under review.We will get back to you soon.")
    created_at = models.DateTimeField(auto_now_add=True)
    ack_no = models.CharField(max_length=10,blank=True)

    def __str__(self):
            return self.tenantFullName

