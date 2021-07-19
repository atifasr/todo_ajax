from django.db import models
from django.db.models.fields import DateTimeField

# Create your models here.


class Tasks(models.Model):
    task_name = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task_name
