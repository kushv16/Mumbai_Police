from random import randint

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import missingPersonInfo
from secret_keys import *
from complaints import views

@login_required
def missingPerson(request):
    secrets = {
        'reCAPTCHA_SITE_KEY': reCAPTCHA_SITE_KEY,
    }
    return render(request,'missingPerson/missingPerson.html', secrets)

def uniqueId():
    uniqueId = 'M'
    for i in range (0,9):
        uniqueId = uniqueId + str(randint(0,9))
    return uniqueId

def missingPerson_form_submission(request):
    firstName = request.POST['firstName']
    lastname = request.POST['lastname']
    gender = request.POST['gender']
    age = request.POST['age']
    color = request.POST['color']
    height = request.POST['height']
    datetime = request.POST['datetime']
    placemissing = request.POST['placemissing']
    police_st = request.POST['police_st']
    desc = request.POST['desc']
    image = request.FILES['image']
    user = request.user
    ack_no = uniqueId()
    missingPerson_info = missingPersonInfo(user=user, firstName=firstName,lastname=lastname,gender=gender,age=age,color=color,
                                          height=height,datetime=datetime,placemissing=placemissing,police_st=police_st,
                                          desc=desc,image=image,ack_no=ack_no)

    views.success(request)
    missingPerson_info.save()
    messages.success(request,f'Your Complaint has been filed and your acknowledgment id is {ack_no}.Our team will shortly get in touch with you.')
    return redirect('home')


def viewMissingPerson(request):
    all_missing_reports = missingPersonInfo.objects.all()
    return render(request,'missingPerson/viewMissingPerson.html',{'Missing':all_missing_reports})