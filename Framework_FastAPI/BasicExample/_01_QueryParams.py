from fastapi import FastAPI
from typing import Optional
import uvicorn

app = FastAPI()

# 1. Optional + None (인자 없어도 됨)
# http://127.0.0.1:8000/add?a=10&b=20 (o)
# http://127.0.0.1:8000/add?b=20 (o)
@app.get("/add")
def get_sum(a:Optional[int]=None, b:int=0): # 기본값
    return a+b

if __name__ == "__main__":
    uvicorn.run("_01_QueryParams:app", reload=True)