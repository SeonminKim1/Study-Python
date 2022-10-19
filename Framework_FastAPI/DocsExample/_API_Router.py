from fastapi import APIRouter


router = APIRouter(
    tags=["model-worker"],
    responses={404 : {"description": "not found"}, 200:{"description": "ok"}},
)

