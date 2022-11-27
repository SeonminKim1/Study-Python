from fastapi import FastAPI
import celery_worker
import uvicorn
import time

app = FastAPI()

@app.get("/worker/add")
async def worker_start(task_id: str, num_1 : int, num_2: int):
    result = celery_worker.add_func.apply_async([num_1, num_2], task_id=task_id)
    print(result.ready()) # False
    time.sleep(3)
    print(result.ready()) # True
    return {"message": "celery start"}

if __name__ == '__main__':
    uvicorn.run('app:app', reload=True)