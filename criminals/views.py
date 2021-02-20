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
    address = request.POST['address']
    pincode = request.POST['pincode']
    prison_sentence = request.POST['prison_sentence']
    current_status = request.POST['current_status']
    datetime = request.POST['datetime']
    crime = request.POST['crime']
    desc = request.POST['desc']
    image = request.FILES['image']

    criminals_info = criminalsInfo(firstname=firstname,lastname=lastname,age=age,gender=gender,address=address,pincode=pincode,prison_sentence=prison_sentence,
                                   current_status=current_status,datetime=datetime,crime=crime,desc=desc,image=image)

    criminals_info.save()

    return HttpResponseRedirect('/')


def ViewCriminals(request):
        all_criminals = criminalsInfo.objects.all()
        return render(request,'criminals/viewCriminals.html',{'Criminals':all_criminals})