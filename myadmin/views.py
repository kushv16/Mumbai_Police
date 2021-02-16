from django.shortcuts import render

# Create your views here.

def myadmin(request):
    return render(request,'myadmin/myadmin.html')

def viewComplaints(request):
    return render(request,'myadmin/viewComplaints.html')