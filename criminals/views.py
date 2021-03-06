from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import criminalsInfo
from criminals.models import criminalsInfo


@login_required
def addCriminals(request):
    return render(request,'criminals/criminals.html')


def addCriminals_form_submission(request):
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    age = request.POST['age']
    gender = request.POST['gender']
    height = request.POST['height']
    prison_sentence = request.POST['prison_sentence']
    current_status = request.POST['current_status']
    date = request.POST['date']
    crime = request.POST['crime']
    desc = request.POST['desc']
    image = request.FILES['image']

    criminals_info = criminalsInfo(firstname=firstname,lastname=lastname,age=age,gender=gender,height=height,prison_sentence=prison_sentence,
                                   current_status=current_status,date=date,crime=crime,desc=desc,image=image)

    criminals_info.save()

    return HttpResponseRedirect('/')


def ViewCriminals(request):
        all_criminals = criminalsInfo.objects.all()
        return render(request,'criminals/viewCriminals.html',{'Criminals':all_criminals})