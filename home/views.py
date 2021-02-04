from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def test(request):
    return render(request, 'home/home.html')