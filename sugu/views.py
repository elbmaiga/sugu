from django.shortcuts import render
from django.http import HttpResponse
from commands.models import *
# Create your views here.

def get_panner(request, user_cookies):
    
    try:
        panner = Panner.objects.get(user_cookies=user_cookies)
    except:
        return 0
    else:
        return HttpResponse("Get panner")
