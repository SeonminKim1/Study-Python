from ninja import Router

router = Router()

# 01.GET
# http://127.0.0.1:8000/api/basic/hello?name=smkim
@router.get("/helloget")
def hello_get(request, name: str = "world"):
    return f"Hello {name}"

# 02.GET QueryParameter
# http://127.0.0.1:8000/api/basic/add?a=1&b=2
@router.get("/add")
def add(request, a: int, b: int):
    return {"result": a + b}

# 03.GET PathParameter
# http://127.0.0.1:8000/api/basic/math/2and3
@router.get("/math/{a}and{b}")
def math(request, a: int, b: int):
    return {"add": a + b, "multiply": a * b}

# 04. POST
from ninja import Schema
class HelloSchema(Schema):
    name: str = "example"

@router.post("/hellopost")
def hello_post(request, data: HelloSchema):
    return f"hello {data.name}"
    