from fastapi import FastAPI, Header
import uvicorn

app = FastAPI()

## Header 
# `X-` 접두어 : 사용자 정의 헤더를 의미하며 표준 헤더와 구분짓기 위해 사용

# http://127.0.0.1:8000/header  Header { X-TOKEN:fighting }
@app.get("/header")
def get_headers(x_token: str = Header(None, title="토큰")):
    return {"X-Token": x_token}

if __name__ == "__main__":
    uvicorn.run("_05_Header:app", reload=True)

