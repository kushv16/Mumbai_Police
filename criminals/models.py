from django.contrib import admin
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
from django.utils import timezone


class criminalsInfo(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('Other', 'Other'),
    )

    CRIMES = (
        ('cyber', 'Cyber'),
        ('extortion', 'Extortion'),
        ('chain snatching', 'Chain Snatching'),
        ('dacotiy', 'Dacoity'),
        ('theft', 'Theft'),
        ('others', 'Others'),
    )

    STATUS=(
        ('in prison','In Prison'),
        ('on bail','On Bail'),
        ('released','Released'),
    )
    firstname = models.CharField(max_length=50,default='null')
    lastname = models.CharField(max_length=50,default='null')
    age = models.PositiveIntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(100)])
    gender = models.CharField(max_length=5, choices=GENDER,default='null')
    address = models.CharField(max_length=100,default='null')
    pincode = models.PositiveIntegerField(default=000000, validators=[MinValueValidator(100000), MaxValueValidator(999999)])
    prison_sentence = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    crime = models.CharField(max_length=50, choices=CRIMES,default='null')
    current_status = models.CharField(max_length=50, choices=STATUS,default='null')
    datetime = models.DateTimeField(blank=True,null=True,default=timezone.now)
    desc = models.CharField(max_length=250,default='null')
    image = models.ImageField(default='default.jpg',upload_to='criminal_pics')


    def __str__(self):
        return self.firstname+" "+self.lastname

