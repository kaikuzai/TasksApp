
from django.urls import path
from . import views 

app_name = 'manager'
urlpatterns = [
    path('', views.index, name='Home'),
    path('tasklist/<int:task_list_id>', views.task_list, name='Task list'),
    path('tasklist/task/<int:task_id>', views.task, name='Task'),
]
