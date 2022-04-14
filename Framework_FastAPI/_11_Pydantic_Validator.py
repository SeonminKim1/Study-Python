## Pydantic
# pydantic 에서 validator decorator를 통한 객체 유효성 검사

from pydantic import BaseModel, ValidationError, validator

class UserModel(BaseModel):
    username: str
    password1: str
    password2: str

    # password2 항목에 대한 유효성 검사
    @validator('password2')
    def passwords_match(cls, v, values, **kwargs):
        if 'password1' in values and v != values['password1']:
            raise ValueError('passwords do not match')
        return v

    # username 항목에 대한 유효성 검사
    @validator('username')
    def username_alphanumeric(cls, v):
        assert v.isalnum(), 'must be alphanumeric'
        return v

user = UserModel(
    username='smkim',
    password1='1a2a3a',
    password2='1a2a3a',
)
print(user) # smkim, 1a2a3a, 1a2a3a

try:
    UserModel(
        username='smkim',
        password1='1a2a3a',
        password2='1a2a3a4a',
    )
except ValidationError as e:
    print(e)