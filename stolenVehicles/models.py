from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class stolenVehiclesInfo(models.Model):
    admin_status = (
        ('under scrutiny', 'Under Scrutiny'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    fullName = models.CharField(max_length=50,blank=True)
    contact = models.CharField(max_length=50,blank=True)
    model_name = models.CharField(max_length=50,blank=True)
    reg_no = models.CharField(max_length=50,blank=True)
    chassis_no = models.CharField(max_length=50,blank=True)
    engine_no = models.CharField(max_length=50,blank=True)
    datetime = models.DateTimeField(blank=True,null=True,default=timezone.now)
    police_station = models.CharField(max_length=50,blank=True)
    desc = models.CharField(max_length=250,blank=True)
    admin_status = models.CharField(max_length=30,choices=admin_status,default='under scrutiny')
    admin_message = models.CharField(max_length=250,default="Your complaint is under review.We will get back to you soon.")
    created_at = models.DateTimeField(auto_now_add=True)
    ack_no = models.CharField(max_length=10,blank=True)

    def __str__(self):
            return self.fullName