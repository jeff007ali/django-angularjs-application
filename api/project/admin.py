from django.contrib import admin
from .models import Projects, Tasks, Subtasks

# Register your models here.
admin.site.register(Projects)
admin.site.register(Tasks)
admin.site.register(Subtasks)
