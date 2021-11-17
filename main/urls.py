from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("blog/",views.blog, name="blog"),
    path("resume/",views.resume, name="resume"),
]