from ninja import ModelSchema
from .models import Article


class ArticleSchemaIn(ModelSchema):
    class Config:
        model = Article
        model_fields = "__all__"


class ArticleSchemaOut(ModelSchema):
    class Config:
        model = Article
        model_fields = "__all__"
