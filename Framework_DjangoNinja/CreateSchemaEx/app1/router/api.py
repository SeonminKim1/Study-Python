from ninja import Router
from django.shortcuts import get_object_or_404

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from app1.models import Task, Category
from app1.schema.create_schema import TaskSchemaOut, TaskSchemaIn, CategorySchema

router = Router()


@router.get("/task", response=TaskSchemaOut)
def get_task(request, task_id: int):
    task = get_object_or_404(Task, id=task_id)
    return task


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
