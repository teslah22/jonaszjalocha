from django.shortcuts import render
from django.http import HttpResponse
from django.utils.regex_helper import normalize
from .models import Clients, ResumeItem


# Create your views here.

def index(response):
    resumeItems = ResumeItem.objects.all().order_by('-JobStart')
    clients = Clients.objects.all()
    return render(response, "main/base.html", {"resumeItems": resumeItems, "clients": clients})

def introduction(response):
    resumeItems = ResumeItem.objects.all().order_by('-JobStart')
    return render(response, "main/base.html", {"resumeItems": resumeItems, "clients": clients})

def resume(response):
    resumeItems = ResumeItem.objects.all().order_by('-JobStart')
    return render(response, "main/base.html", {"resumeItems": resumeItems, "clients": clients})

def clients(response):
    resumeItems = ResumeItem.objects.all().order_by('-JobStart')
    return render(response, "main/base.html", {"resumeItems": resumeItems, "clients": clients})

def projects(response):
    resumeItems = ResumeItem.objects.all().order_by('-JobStart')
    return render(response, "main/base.html", {"resumeItems": resumeItems, "clients": clients})

def contact(response):
    resumeItems = ResumeItem.objects.all().order_by('-JobStart')
    return render(response, "main/base.html", {"resumeItems": resumeItems, "clients": clients})


