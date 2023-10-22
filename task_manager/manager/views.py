from django.shortcuts import render
from . import models

# Create your views here.
def index(request):
    all_lists = models.TaskList.objects.all()
    context = {
        'all_lists':all_lists
    }
    return render(request, 'manager/index.html', context)

def task_list(request, task_list_id):
    context = {
        'task_list_id':task_list_id
    }
    return render(request, 'manager/task-list.html', context)


def task(request, task_id):
    context = {
        'task_id':task_id
    }
    return render(request, 'manager/task.html', context)