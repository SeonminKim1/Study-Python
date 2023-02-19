from ninja import NinjaAPI

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from app1.api import router as app1_router

api = NinjaAPI()
api.add_router("/app1/", app1_router)
