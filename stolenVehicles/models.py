from django.db import models
from django.utils import timezone


class stolenVehiclesInfo(models.Model):
    admin_status = (
        ('under scrutiny', 'Under Scrutiny'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )

    fullName = models.CharField(max_length=50,default='null')
    contact = models.CharField(max_length=50,default='null')
    model_name = models.CharField(max_length=50,default='null')
    reg_no = models.CharField(max_length=50,default='null')
    chassis_no = models.CharField(max_length=50,default='null')
    engine_no = models.CharField(max_length=50,default='null')
    datetime = models.DateTimeField(blank=True,null=True,default=timezone.now)
    police_station = models.CharField(max_length=50,default='null')
    desc = models.CharField(max_length=250,default="null")
    admin_status = models.CharField(max_length=30,choices=admin_status,default='under scrutiny')

    def __str__(self):
        return self.fullName