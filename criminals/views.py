from django.shortcuts import render

def criminals(request):
    return render(request,'criminals/criminals.html')