from ninja import Router
from .schema import TaskSchemaNoValidIn, TaskSchemaValidIn, TaskSchemaNoValidOut, TaskSchemaValidOut
from .models import Task
from typing import List
from django.shortcuts import get_object_or_404

router = Router()

'''
Request Test
'''
@router.post("/task/novalid", response=TaskSchemaNoValidOut)
def create_task_no_valid(request, payload: TaskSchemaNoValidIn):
    task = Task.objects.create(**payload.dict())
    print(task, type(task))
    return task # {'success':True}


@router.post("/task/valid", response=TaskSchemaNoValidOut)
def create_task_valid(request, payload: TaskSchemaValidIn):
    task = Task.objects.create(**payload.dict())
    print(task, type(task))
    return task # {'success':True}

'''
Response Test
'''
@router.get("/task/valid", response=TaskSchemaValidOut)
def get_task_valid(request, task_id: int):
    task = get_object_or_404(Task, id=task_id)
    print(task, type(task))
    return task


@router.get("/task/novalid", response=TaskSchemaNoValidOut)
def get_task_no_valid(request, task_id: int):
    task = get_object_or_404(Task, id=task_id)
    print(task, type(task))
    return task


@router.get("/tasks/", response=List[TaskSchemaValidOut])
def get_task_list(request):
    tasks = Task.objects.all()
    print(tasks)
    return tasks

