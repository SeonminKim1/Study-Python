
## Queryset과 Object 차이
- Queryset 은 DB의 데이터 값을 ORM형태로 변환하여 읽어들인 것 (Django ORM의 자료형)이며, Python 자체의 Object 자료형 범위와는 약간 상이하다.
- 따라서 파이썬에서 해당 ORM 자료형을 사용하기 위해서는 Python Object(or 자료형)로 형변환이 필요하다. 
- 정리하면 Django ORM (Django Model)으로 DB값 조회 => Queryset 반환 => Python 자료형으로 형변환의 Flow를 거쳐 사용 된다.