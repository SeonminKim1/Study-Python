from fastapi import Depends, FastAPI, HTTPException

app = FastAPI()

#############
# Depends (입력 종속성 관련 라이브러리)
# Depends (Class or Function)
# HTTPException (접근 의존성 부여)
# 사용자용 의존성, 관리자 의존성
#############

async def common_parameters(id: str, name: str, age: int):
    return {"id": id, "name": name, "age": age}

class CommonQueryParams:
    def __init__(self, id: str, name: str, age: int):
        self.id = id; self.name = name; self.age = age

# HTTPExeption
async def verify_age(commons: CommonQueryParams = Depends(CommonQueryParams)):
    if commons.age < 18:
        raise HTTPException(status_code=400, detail="Requires adult supervision")

async def verify_admin(commons: CommonQueryParams = Depends(CommonQueryParams)):
    if commons.id != 'ID0001':
        raise HTTPException(status_code=400, detail="Requires admin access")

# 사용자용 의존성
@app.get("/user/", dependencies=[Depends(verify_age)])
async def user(commons: dict = Depends(common_parameters)): # depends :
    return commons

# 관리자 의존성
@app.get("/admin/", dependencies=[Depends(verify_admin), Depends(verify_age)])
async def admin(commons: dict = Depends(common_parameters)):
    return commons

# http://localhost:8000/admin/?id=ID0001&name=wfng&age=18
# http://localhost:8000/admin/?id=ID0001&name=wfng&age=15 # HTTPException Error