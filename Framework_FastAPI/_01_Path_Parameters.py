from fastapi import FastAPI
from enum import Enum

# POST에서는 Pydantic
# GET에서는 Enum

app = FastAPI()

class Model(str, Enum):
    alexnet = 'alexnet',
    resnet = 'resnet',

# 1. 일반 Path기반 Parameters
# http://127.0.0.1:8000/model/alexnet
# http://127.0.0.1:8000/model/resnet
@app.get("/model/{model_id}")
async def get_model(model_id: Model):
    if model_id == Model.alexnet:
        return {'m': model_id}

    elif model_id == Model.resnet:
        return {'m': model_id}

    return {'m':'Nothing'}

# 2. Query 스트링
# ?로 시작 알림, &로 복수개의 Parameters 지정
# http://127.0.0.1:8000/add/?a=10&b=20
# http://127.0.0.1:8000/add/?a=10&b=20
# 
# curl http://127.0.0.1:8000/inference/4-5 
# @app.get("/inference/{job_id}-{dok_id}")

# curl http://127.0.0.1:8000/inference2/4?dok_id=5
# @app.get("/inference2/{job_id}")

@app.get("/add/")
async def get_sum(a:int, b:int):
    return {'두 수의 합은':a+b}
    
