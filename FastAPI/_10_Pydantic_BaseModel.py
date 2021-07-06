
## Pydantic
# pydantic 에서 BaseModel을 통해 객체를 정의
# 모델 인스턴스의 필드가 모델에 정의 된 필드 유형을 준수 함을 보장
# pydantic 은 입력 데이터가 아닌 출력 모델의 유형과 제약 조건을 보장 !

from pydantic import BaseModel

class User(BaseModel):
    id: int
    name = 'Jane Doe'

if __name__ == "__main__":
    user = User(id = '123') # 자동 int로 cast 됨
    print(type(user.id), user.id)
    print(user.id == 123, user.id == '123')
