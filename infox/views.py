from atexit import register
import json
from .models import *
from django.http import BadHeaderError
from django.shortcuts import redirect, render
from urllib import request
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate ,login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import HttpResponse
from django.core.mail import send_mail,BadHeaderError
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

def load_homepage(request):
    return render(request,'home.html')
def load_bease(request):
    return render(request,'base.html')
def load_mobile(request):
    return render(request,'mobile.html')
def load_csm(request):
    return render(request,'csm.html')


#sending mail
@csrf_exempt
def sending_mail(request):
    if request.method == 'POST': 
        recipient = request.POST['smailid'] 
        message="Your message has been sent. Thank you!"
        sendsubject="INFINITYFOX Technologies"
        try:
            respons=send_mail(sendsubject, message,settings.EMAIL_HOST_USER,[recipient])
            return render(request,'sendmailout.html',{'message':message})
            
        except BadHeaderError:
            return()
