from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import missingPersonInfo
# Create your views here.

@login_required
def missingPerson(request):
    return render(request,'missingPerson/missingPerson.html')


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
    image = request.POST['image']
    user = request.user
    missingPerson_info = missingPersonInfo(user=user, firstName=firstName,lastname=lastname,gender=gender,age=age,color=color,
                                          height=height,datetime=datetime,placemissing=placemissing,police_st=police_st,
                                          desc=desc,image=image)

    missingPerson_info.save()
    return HttpResponseRedirect('/')

def viewMissingPerson(request):
    all_missing_reports = missingPersonInfo.objects.all()
    return render(request,'missingPerson/viewMissingPerson.html',{'Missing':all_missing_reports})