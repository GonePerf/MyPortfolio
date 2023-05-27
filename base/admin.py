from django.contrib import admin

# Register your models here.

from .models import Tool, Topic, Message, Project

admin.site.register(Tool)
admin.site.register(Project)
admin.site.register(Topic)
admin.site.register(Message)