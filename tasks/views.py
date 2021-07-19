
import json
from django.db.models.expressions import OrderBy
from django.http.response import JsonResponse
from django.shortcuts import render
from .models import Tasks
from django.core.exceptions import *

from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from api.serializers import TaskSerializer
from rest_framework import status
# Create your views here.


def tasks(request):
    return render(request, 'todo/tasks.html')


def get_tasks(request):
    data = []
    if request.method == 'GET':
        result = {'exist': False}
        try:
            tasks = Tasks.objects.all().values().order_by('time')
            # print(tasks)
            result['exist'] = True
        except(EmptyResultSet):
            result['exist'] = False
            return JsonResponse(result, safe=False)

        for val in tasks:
            data.append(val)
        # print(data)
    return JsonResponse(data, safe=False)


# @csrf_exempt
def add_task(request):
    if request.method == 'GET':
        val = request.GET.get('task')
        tasks = Tasks(task_name=val)
        tasks.save()
        print(tasks)
        serialized_task=TaskSerializer(tasks)
        print(serialized_task.data)

        return JsonResponse(serialized_task.data,safe=False)


def remove_task(request):
    if request.method == 'GET':
        filter_ = request.GET.get('id')
        try:
            task=Tasks.objects.get(id=filter_)
            task.delete() 
            deleted_task=TaskSerializer(task)
        except(ObjectDoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)
        return JsonResponse({'data':deleted_task.data,'message':'objects deleted'})
    


def update_task(request):
    if request.method == 'GET':
        id_ = request.GET.get('id')
        print(request.GET.get('text'))
        print(id_)
        tasks=Tasks.objects.get(id=id_)
        tasks.task_name = request.GET.get('text')
        tasks.save()
        return JsonResponse({'updated_data':'tasks','status':'good'})