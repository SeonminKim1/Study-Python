import pytest

class Fruit:
    def __init__(self, name):
        self.name = name

# 만약 fixture를 안붙으면 pytest가 인식 못함 사용 불가
@pytest.fixture
def my_fruit():
    return Fruit("apple")

@pytest.fixture
def fruit_basket(my_fruit): # 위의 my_fruit 함수 담음.
    return [Fruit("banana"), my_fruit]

# 위의 두개 함수 담음
def test_my_fruit_in_basket(my_fruit, fruit_basket): 
    assert my_fruit in fruit_basket # fruit_basket에 my_fruit이 있는지 확인하기 위해 fixture를 만든 것.