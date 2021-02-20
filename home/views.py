from django.shortcuts import render
from geo import load_layer
from missingPerson import models
from django.http import HttpResponse
from missingPerson.models import missingPersonInfo
from complaints.models import complaintsInfo
from verification.models import VerificationInfo
from stolenVehicles.models import stolenVehiclesInfo


def home(request):
    return render(request, 'home/home.html')



def status(request):
    user_id = request.user.id
    missing_person = missingPersonInfo.objects.filter(user_id=user_id)
    complaints = complaintsInfo.objects.filter(user_id=user_id)
    verification = VerificationInfo.objects.filter(user_id=user_id)
    return render(request,'home/status.html', {'Missing':missing_person})
