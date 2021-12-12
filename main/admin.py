from django.contrib import admin
from .models import PostItem
from .models import ResumeItem
from .models import Clients

admin.site.register(PostItem)
admin.site.register(ResumeItem)
admin.site.register(Clients)