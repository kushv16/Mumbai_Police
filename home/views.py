from django.shortcuts import render
from geo import load_layer

# Create your views here.
from django.http import HttpResponse

def home(request):
    # load_layer.run()
    return render(request, 'home/home.html')