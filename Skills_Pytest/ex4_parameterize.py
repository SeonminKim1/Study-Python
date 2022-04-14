# 파라미터 인자를 직접 테스트 코드에 전달하기

import pytest
# 리스트로 다수의 파라미터 인자를 전달하여 다수 케이스에 대한 테스트
# parametrize로 파라미터와 해당 값 전달
@pytest.mark.parametrize("test_input, expected", [("3+5", 8), ("2+4", 6), ("6*7", 42)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected

