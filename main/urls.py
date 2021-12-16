from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("introduction/",views.introduction, name="introduction"),
    path("resume/",views.resume, name="resume"),
    path("clients/",views.clients, name="clients"),
    path("projects/",views.projects, name="projects"),
    path("contact/",views.contact, name="contact"),
]