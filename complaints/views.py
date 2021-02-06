from django.shortcuts import render

from django.http import HttpResponse

def complaints(request):
    return render(request,'complaints/complaints.html')