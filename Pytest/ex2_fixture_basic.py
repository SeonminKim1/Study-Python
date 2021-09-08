# 함수를 변수 처럼 사용.
# params : 반복문 같은 느낌
# Pytest fixture의 params 인수를 활용 - 다수의 fixture 값을 생성하여 테스트
import pytest

@pytest.fixture
def square_10():
    return 10 * 10

def test_square(square_10):
    assert square_10 == 100 # 121

@pytest.fixture(params=[1, 3]) # params 반복문 같은 느낌
def make_double_value(request):
    # 기능 = params에 대해 2개의 값을 return
    print('make_double_value', request)
    return (request.param, request.param * 2)

# make double value에서 반환하는 2가지 값에 대해 비교
def test_double_value(make_double_value):
    assert make_double_value[1] == (make_double_value[0] * 2)