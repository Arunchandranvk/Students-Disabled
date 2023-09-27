from django.contrib import admin
from .models import *
from django.contrib.admin.models import LogEntry
from django.contrib.auth import get_user_model
from django.db import models

class CustomLogEntry(LogEntry):
    # Use your custom user model for the user field
    CustUser = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, blank=True, null=True)

# Register the custom LogEntry model with the admin site
admin.site.register(CustomLogEntry)

# Register your models here.

admin.site.register(Subjects)
admin.site.register(Student)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Category)
admin.site.register(Suggestion)
admin.site.register(StudentAnswer)
admin.site.register(CustUser)
