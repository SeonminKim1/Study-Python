from ninja import Schema
from pydantic import BaseModel, validator


'''
Request Test
'''
# Q1. Request Validation 불필요
class TaskSchemaNoValidIn(Schema):
    id: int
    title: str


# Q2. Request Validation 필요
class TaskSchemaValidIn(BaseModel):
    id: int
    title: str

    @validator('title', always=True)
    def title_length_check(cls, v) -> str:
        if len(v) >= 3:
            return v
        return None


# Q3. Response Validation 불필요
class TaskSchemaNoValidOut(Schema):
    id: int
    title: str


# Q4. Response Validation 필요
class TaskSchemaValidOut(Schema):
    id: int
    title: str

    @staticmethod
    def resolve_title(obj):
        return 'ive_' + obj.title
