from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import VerificationInfo
from secret_keys import *

@login_required
def verification(request):
    secrets = {
        'reCAPTCHA_SITE_KEY': reCAPTCHA_SITE_KEY,
    }
    return render(request,'verification/verification.html', secrets)


def verification_form_submission(request):
    propOwnerFullName = request.POST['propOwnerFullName']
    propOwnerContact = request.POST['propOwnerContact']
    propOwnerEmail = request.POST['propOwnerEmail']
    propOwnerFlatno = request.POST['propOwnerFlatno']
    propOwnerAddress = request.POST['propOwnerAddress']
    propOwnerCity = request.POST['propOwnerCity']
    propOwnerState = request.POST['propOwnerState']
    propOwnerCountry = request.POST['propOwnerCountry']
    tenantFullName = request.POST['tenantFullName']
    tenantContact = request.POST['tenantContact']
    tenantEmail = request.POST['tenantEmail']
    tenantFlatno = request.POST['tenantFlatno']
    tenantAddress = request.POST['tenantAddress']
    tenantCity = request.POST['tenantCity']
    tenantState = request.POST['tenantState']
    tenantCountry = request.POST['tenantCountry']
    tenantDOB = request.POST['tenantDOB']
    tenantReason = request.POST['tenantReason']
    tenantOrganisation = request.POST['tenantOrganisation']
    tenantDepartment = request.POST['tenantDepartment']
    tenantID = request.POST['tenantID']
    tenantInstitute = request.POST['tenantInstitute']
    tenantBranch = request.POST['tenantBranch']
    desc = request.POST['desc']
    user = request.user

    verification_info = VerificationInfo(user=user,propOwnerFullName=propOwnerFullName,propOwnerContact=propOwnerContact,propOwnerEmail=propOwnerEmail,
                                         propOwnerFlatno=propOwnerFlatno,propOwnerAddress=propOwnerAddress,propOwnerCity=propOwnerCity,
                                         propOwnerState=propOwnerState,propOwnerCountry=propOwnerCountry,tenantFullName=tenantFullName,
                                         tenantContact=tenantContact,tenantEmail=tenantEmail,tenantFlatno=tenantFlatno,tenantAddress=tenantAddress,
                                         tenantCity=tenantCity,tenantState=tenantState,tenantCountry=tenantCountry,tenantDOB=tenantDOB,tenantReason=tenantReason,
                                         tenantOrganisation=tenantOrganisation,tenantDepartment=tenantDepartment,tenantID=tenantID,tenantInstitute=tenantInstitute,
                                         tenantBranch=tenantBranch,desc=desc)

    verification_info.save()
    return HttpResponseRedirect('/')