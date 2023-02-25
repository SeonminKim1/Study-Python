from ninja import Router
from .models import Article
from. schema import ArticleSchemaIn, ArticleSchemaOut
from typing import List
from ninja.pagination import paginate, PageNumberPagination, LimitOffsetPagination

router = Router()


@router.post("/create", response=str)
def create_article(request, payload:ArticleSchemaIn):
    Article.objects.create(**payload.dict())
    return 'success'

# /api/app1/view/article/pagenumber?page=3
@router.get("/view/article/pagenumber", response=List[ArticleSchemaOut])
@paginate(PageNumberPagination, page_size=3)
def get_article_pagenumber(request):
    return Article.objects.all()


# /api/app1/view/article/limitoffset?limit=5&offset=2
@router.get("/view/article/limitoffset", response=List[ArticleSchemaOut])
@paginate(LimitOffsetPagination)
def get_article_limit_offset(request):
    return Article.objects.all()