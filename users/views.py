from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse

def register(request):
    if(request.method == 'POST'):
        form = UserRegisterForm(request.POST)
        if(form.is_valid()):
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            user = User.objects.get(username=username)
            token = RefreshToken.for_user(user).access_token
            current_site = get_current_site(request).domain
            relativeLink = reverse('verify-email')
            absurl = 'http://'+current_site+relativeLink+"?token="+str(token)
            email_body = 'Hi '+user.username+' use link below to verify your email \n'+absurl
            data = {
                'to': email,
                'email_body': email_body,
                'email_subject': 'Verify your email'
            }
            Util.send_email(data)
            messages.success(request, f'Your Account has been Created! You can now Login {username}!')
            return redirect('login')
    else :
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})


def verifyEmail():
    pass



