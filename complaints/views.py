from django.shortcuts import render
from .forms import ComplaintForm
from django.http import HttpResponse, HttpResponseRedirect


def complaints(request):
    return render(request,'complaints/complaints.html')

def upload_form(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return HttpResponseRedirect('')
    else:
        form = ComplaintForm()
    return render(request, 'complaints.html', {'form': form})