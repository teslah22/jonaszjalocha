from django.contrib import admin
from .models import PostItem
from .models import ResumeItem

admin.site.register(PostItem)
admin.site.register(ResumeItem)