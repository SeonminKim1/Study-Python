import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from app1.models import Task, Category
from ninja.orm import create_schema

TaskSchemaIn = create_schema(
    Task,
    fields=['id', 'title', 'category'],
    # depth=1 # for category
)

TaskSchemaOut = create_schema(
    Task,
    exclude=['id'], # 'title','category'
    depth=1,
)

CategorySchema = create_schema(
    Category,
    fields = ['id', 'type']
)
'''
# Validator 불가 - 미구현됨
# __validators__= https://github.com/vitalik/django-ninja/blob/5dac89c59cf0371fa3ed51906072c4a9b7db2309/ninja/orm/factory.py#L71 
'''


# CategorySchemaOut = create_schema(
#     Category,
#     fields = ['id', 'type', 'task'],
#     custom_fields=[
#         ('url', str, None), # Optional[List[Tuple[str, Any, Any]]] = None,
#     ],
# )