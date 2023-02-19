from ninja import ModelSchema

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from app1.models import Task, Category

class CategorySchema(ModelSchema):
    class Config:
        model = Category
        model_fields = ['id', 'type']
class TaskSchemaOut(ModelSchema):
    category: CategorySchema
    class Config:
        model = Task
        # model_fields = ['title']
        # model_exclude = ['id', ]
        model_fields = "__all__"

    @staticmethod
    def resolve_title(obj):
        return 'ive_' + obj.title
class TaskSchemaIn(ModelSchema):
    class Config:
        model = Task
        model_fields = ["id", "title", 'category']
