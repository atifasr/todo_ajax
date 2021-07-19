from django.db import models
from django.db.models import fields
from rest_framework import serializers
from tasks.models import *



class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'
