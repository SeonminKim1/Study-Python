from ninja import Router

router = Router()

@router.get("/helloget")
def hello_get(request, name: str = "world"):
    return f"Hello {name}"
