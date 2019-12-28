from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Projects(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=300)
    duration = models.IntegerField()
    avatar = models.TextField(null=True)

    def __str__(self):
        return "{} - {}".format(self.name, self.duration)

class Tasks(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=300)
    startDate = models.IntegerField(null=False)
    endDate = models.IntegerField()
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    assignee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "{} - {}".format(self.name, self.project.name)

class Subtasks(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=300)
    startDate = models.IntegerField(null=False)
    endDate = models.IntegerField()
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.name, self.task.name)

