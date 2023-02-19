import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from ninja import Router

router = Router()

@router.get("/helloget")
def hello_get(request, name: str = "world"):
    return f"Hello {name}"
