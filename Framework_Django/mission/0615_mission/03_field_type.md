
## Primary Key (기본키)
- 해당 레코드를 식별 할 수 있는 속성의 최소 집합.
- 한 개의 Table 에서 반드시 하나만 존재 해야 함.
- Django는 pk 지정 안할 시 기본적으로 auto-incrementing primary key를 만들어줌 (필드명 : id)
- Django에서 pk 지정시 primary_key = True로 가능

## Foreign Key (외래키)
- 외래키는 다른 테이블의 기본키를 참조하는 속성을 일컫으
- 다른 테이블의 기본키를 참조하여, RDB 간의 관계를 표현
- One-to-One, One-to-Many, Many-to-Many 등의 관계가 있음

## Unique Key
- 테이블 내에서 특정 필드값이 레코드별로 유일한 값을 가지게 지정하는 경우
- Django에서는 unique=True 등으로 설정 가능
- 여러개의 컬럼 값을 묶어 Unique 집합으로 사용 가능.
