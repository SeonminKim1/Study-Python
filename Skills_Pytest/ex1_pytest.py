# python
import pytest

# test_sample.py . : Test가 성공했음을 의미
# test_sample.py F : Test가 실패했음을 의미
def func(x):
    return x + 1

def test_answer1():
    assert func(3) == 4

def test_even():
    a = 12
    assert a % 2 == 0, "value was odd, should be even"