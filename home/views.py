from django.shortcuts import render
from geo import load_layer
from missingPerson import models
from django.http import HttpResponse
from missingPerson.models import missingPersonInfo

def home(request):
    # load_layer.run()
    return render(request, 'home/home.html')


def status(request):
    user_id = request.user.id
    missing_person = missingPersonInfo.objects.all()
    missing_dict = {};
    missing_list = [];
    for missing in missing_person.iterator():
        if(missing.user_id==user_id):
            missing_list.append(missing.firstName)
            print(missing_dict)
    missing_dict['first_name']=missing_list

    return render(request,'home/status.html',missing_dict)