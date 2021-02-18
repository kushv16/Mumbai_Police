from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import missingPersonInfo
# Create your views here.

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

    missingPerson_info = missingPersonInfo(firstName=firstName,lastname=lastname,gender=gender,age=age,color=color,
                                          height=height,datetime=datetime,placemissing=placemissing,police_st=police_st,
                                          desc=desc)

    missingPerson_info.save()

    return HttpResponseRedirect('/')