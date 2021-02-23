from random import randint

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import stolenVehiclesInfo
import os
@login_required
def stolenVehicles(request):
    secrets = {
        'reCAPTCHA_SITE_KEY': os.environ.get('reCAPTCHA_SITE_KEY'),
    }
    return render(request,'stolenVehicles/stolenVehicles.html', secrets)

def uniqueId():
    uniqueId = 'S'
    for i in range (0,9):
        uniqueId = uniqueId + str(randint(0,9))
    return uniqueId

def stolenVehicles_form_submission(request):
    fullName = request.POST['fullName']
    contact = request.POST['contact']
    model_name = request.POST['model_name']
    reg_no = request.POST['reg_no']
    chassis_no = request.POST['chassis_no']
    engine_no = request.POST['engine_no']
    datetime = request.POST['datetime']
    police_station = request.POST['police_station']
    desc = request.POST['desc']
    user = request.user
    ack_no = uniqueId()
    stolenVehicles_info = stolenVehiclesInfo(user=user,fullName=fullName,contact=contact,model_name=model_name,
                                             reg_no=reg_no,chassis_no=chassis_no,engine_no=engine_no,
                                             datetime=datetime,police_station=police_station,desc=desc,ack_no=ack_no)

    stolenVehicles_info.save()
    messages.success(request,f'Your Complaint has been filed and your acknowledgment id is {ack_no}.Our team will shortly get in touch with you.')
    return redirect('home')