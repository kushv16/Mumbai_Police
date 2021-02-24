from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer

from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
import jwt
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status


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
            relativeLink = reverse('login')
            absurl = 'http://'+current_site+relativeLink+"?token="+str(token)
            email_body = 'Hi '+user.username+' use link below to verify your email \n'+absurl
            data = {
                'to': email,
                'email_body': email_body,
                'email_subject': 'Verify your email'
            }
            Util.send_email(data)
            return redirect('verify-email')
    else :
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

def verify_email_page(request):
    return render(request, 'users/verify_email_page.html')


def verifyEmail(request):
    token = request.GET.get('token')
    try:
        payload = jwt.decode(token, settings.SECRET_KEY)
        user = User.objects.get(id=payload['user_id'])
        if not user.is_authenticated:
            user.is_authenticated = True
            user.save()
        messages.success(request, f'Your Account has been Authenticated! You can now Login {user.username}!')
        return redirect('login')

    except jwt.ExpiredSignatureError as expired:
        return Response({'error': 'Activation Expired'}, status=status.HTTP_400_BAD_REQUEST, template_name='blah.html')

    except jwt.exceptions.DecodeError as invalid:
        return Response({'error': 'Invalid Token'}, status=status.HTTP_400_BAD_REQUEST)

    except :
        return Response({'error': 'Error'}, status=status.HTTP_400_BAD_REQUEST)




