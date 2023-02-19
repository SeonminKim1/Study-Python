from ninja import Router
from .schema.model_schema import TaskSchemaOut, TaskSchemaIn, CategorySchema
from .models import Task, Category
from typing import List
from django.shortcuts import get_object_or_404

router = Router()


@router.get("/task/", response=TaskSchemaOut)
def get_task(request, task_id: int):
    task = get_object_or_404(Task, id=task_id)
    print(task, type(task))
    return task

@router.get("/tasks/", response=List[TaskSchemaOut])
def get_tasks(request):
    tasks = Task.objects.all()
    print(tasks, type(tasks))
    return tasks

@router.post("/task/", response = TaskSchemaOut)
def create_task(request, payload: TaskSchemaIn):
    payload_dict = payload.dict()
    task = Task.objects.create(
        id = payload_dict['id'],
        title = payload_dict['title'],
        category = Category.objects.get(id = int(payload_dict['category']))
    )
    print(task, type(task))
    return task # {'success':True}


@router.post("/category/", response=CategorySchema)
def create_category(request, payload: CategorySchema):
    category = Category.objects.create(**payload.dict())
    print(category, type(category))
    return category

