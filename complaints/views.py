from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import complaintsInfo
from random import randint
from secret_keys import *
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from complaints import models

@login_required
def complaints(request):
    secrets = {
        'reCAPTCHA_SITE_KEY' : reCAPTCHA_SITE_KEY,
    }
    return render(request,'complaints/complaints.html', secrets)


def uniqueId():
    uniqueId = 'C'
    for i in range (0,9):
        uniqueId = uniqueId + str(randint(0,9))
    return uniqueId

def success(request):
    template = render_to_string('home/email_template.html',{'name':request.user.username})
    email = EmailMessage(
        'Your Complaint has been filed',
        template,
        settings.EMAIL_HOST_USER,
        [request.user.email],
    )
    email.fail_silently=False
    email.send()

def complaints_form_submission(request):
    fullName = request.POST['fullName']
    contact = request.POST['contact']
    email = request.POST['email']
    flatno = request.POST['flatno']
    address = request.POST['address']
    city = request.POST['city']
    state = request.POST['state']
    country = request.POST['country']
    datetime = request.POST['datetime']
    crime = request.POST['crime']
    desc = request.POST['desc']
    user = request.user
    ack_no = uniqueId()
    complaints_info = complaintsInfo(user=user,fullName=fullName, contact=contact, email=email, flatno=flatno, address=address,
                                 city=city, state=state, country=country, datetime=datetime, crime=crime, desc=desc , ack_no=ack_no)

    complaints_info.save()
    success(request)
    messages.success(request,f'Your Complaint has been filed and your acknowledgment id is {ack_no}.Our team will shortly get in touch with you.')
    return redirect('home')
