from django.shortcuts import render
from django.http import HttpResponse
from django.utils.regex_helper import normalize
from .models import ResumeItem, PostItem


# Create your views here.

def index(response):
    return render(response, "main/base.html", {})

def resume(response):
    resumeItems = ResumeItem.objects.all().order_by('-JobStart')
    return render(response, "main/resume.html", {"resumeItems": resumeItems})

def blog(response):
    posts = PostItem.objects.all()
    return render(response, "main/blog.html", {"posts": posts})

