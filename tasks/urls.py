from django.urls import path
from django.urls.resolvers import URLPattern
from .views import *

app_name = 'todo'

urlpatterns = [
    path('tasks/', tasks),
    path('get_tasks/', get_tasks, name='get-tasks'),
    path('add_task/', add_task),
    path('remove_task/', remove_task),
    path('update_task/', update_task),
]
