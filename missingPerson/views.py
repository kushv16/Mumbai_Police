from django.shortcuts import render

# Create your views here.

def missingPerson(request):
    return render(request,'missingPerson/missingPerson.html')