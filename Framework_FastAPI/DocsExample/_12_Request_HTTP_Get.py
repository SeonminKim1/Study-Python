from fastapi import FastAPI
from typing import Optional

app = FastAPI()

# uvicorn FastAPI_Request:app --reload

@app.get("/")
async def read_root():
    return {"Hello": "World"}

# case 1
# curl http://127.0.0.1:8000/inference/4-5
@app.get("/inference/{job_id}-{dok_id}")
async def start_inference_with_docker(job_id: int,
                                      dok_id :int):
    return {"job_id": job_id, "dok_id":dok_id}

# case 2
# curl http://127.0.0.1:8000/inference2/4?dok_id=5
@app.get("/inference2/{job_id}")
async def start_inference_with_docker(job_id: int,
                                      dok_id :Optional[int]=None):
    return {"job_id": job_id, "dok_id":dok_id}