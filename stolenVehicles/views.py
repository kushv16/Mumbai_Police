from django.shortcuts import render

def stolenVehicles(request):
    return render(request,'stolenVehicles/stolenVehicles.html')