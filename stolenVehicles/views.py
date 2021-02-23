from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import stolenVehiclesInfo
from secret_keys import *

@login_required
def stolenVehicles(request):
    secrets = {
        'reCAPTCHA_SITE_KEY': reCAPTCHA_SITE_KEY,
    }
    return render(request,'stolenVehicles/stolenVehicles.html', secrets)

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
    stolenVehicles_info = stolenVehiclesInfo(user=user,fullName=fullName,contact=contact,model_name=model_name,
                                             reg_no=reg_no,chassis_no=chassis_no,engine_no=engine_no,
                                             datetime=datetime,police_station=police_station,desc=desc)

    stolenVehicles_info.save()

    return HttpResponseRedirect('/')