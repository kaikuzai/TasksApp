from django.db import models

# Create your models here.

class TaskList(models.Model):
    task_list_name = models.CharField(max_length=50)
    pub_date = models.DateTimeField("date published")

    def __str__(self) -> str:
        return self.task_list_name


class Task(models.Model):
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=50)
    task_desc = models.CharField(max_length=200)

    # Estimated time it will take to complete the task 
    task_time = models.IntegerField(default=0)


    def __str__(self) -> str:
        return self.task_name

class SubTask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    sub_task_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.sub_task_name