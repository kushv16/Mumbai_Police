"""Mumbai_Police URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
from complaints import views as complaints_views
from criminals import views as criminal_views
from eChallan import views as eChallan_views
from missingPerson import views as missingPerson_views
from stolenVehicles import views as stolenVehicles_views
from verification import views as verification_views
from home import views as home_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('complaints/', include('complaints.urls')),
    path('complaints/complaints_form_submission',complaints_views.complaints_form_submission,name='complaints_form_submission'),
    path('', include('home.urls')),
    path('geo/', include('geo.urls')),
    path('addCriminals/addCriminals_form_submission',criminal_views.addCriminals_form_submission,name='addCriminal_form_submission'),
    path('viewCriminals',criminal_views.ViewCriminals,name='view-criminal'),
    path('eChallan/',eChallan_views.eChallan,name='e-challan'),
    path('missingPerson/',missingPerson_views.missingPerson,name='missing-person'),
    path('missingPerson/missingPerson_form_submission/',missingPerson_views.missingPerson_form_submission,name='missingPerson_form_submission'),
    path('viewMissingPerson',missingPerson_views.viewMissingPerson,name='view-missing-person'),
    path('stolenVehicles/',stolenVehicles_views.stolenVehicles,name='stolen-vehicles'),
    path('stolenVehicles/stolenVehicles_form_submission',stolenVehicles_views.stolenVehicles_form_submission,name='stolenVehicles_form_submission'),
    path('verification/',verification_views.verification,name='verification'),
    path('verification/verification_form_submission', verification_views.verification_form_submission, name='verification_form_submission'),
    path('status',home_views.status,name='status'),
]+static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
