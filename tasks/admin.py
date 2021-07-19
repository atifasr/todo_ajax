from django.contrib import admin
from django.db.models import fields
from .models import *

# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    fields = ('task_name', 'time')


admin.site.register(Tasks, TaskAdmin)
