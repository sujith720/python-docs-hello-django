from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("*****Hello Amdocs Team - Good evening, we are all learning jenkins & CI CD DevOPS + we are all Happy****** ")
