from django.contrib import admin

# Register your models here.

from .models import Skill, Topic, Message, Project

admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Topic)
admin.site.register(Message)