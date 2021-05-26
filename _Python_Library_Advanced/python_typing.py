
# python Type Annotation, 타입 힌팅
## Type annotation
# Python은 동적 타이핑 언어
# 동적 타이핑은 이렇게 단순한 코드를 만들 수 있지만, 변수에 전달되는 값이 과연 원하는 것으로 전달되는 지를 감시할 수 없다


# List, Dict, Tuple, Set
from typing import List, Dict, Tuple, Set

nums:List[int] = [1,2,3]
countries: Dict[str,str]={'kr':'south-korea','us':'united-states'}
user : Tuple[int, str, bool] = (3, 'smkim',True)
chars: Set[str] = {"A", "B", "A","C"}
print('Typing')
print(nums, countries, user, chars)

# Final, Union
from typing import Final, Union
print('Final, Union')
TIME_OUT: Final[int] = 10
print(TIME_OUT)

# Union은 여러 개의 타입이 허용될 수 있는 상황
def toString(num: Union[int, float]) -> str:
    return str(num)
print(toString(1))

from typing import Optional
# typing 모듈의 Optional은 None이 허용되는 함수의 매개 변수에 대한 타입을 명시할 때 유용
# Optional[int]는 Union[int, None]과 동일
def repeat(message: str, times: Optional[int] = None) -> list:
    if times:
        return [message] * times
    else:
        return [message]

print('Optional')
print(repeat('hi',3))

## 참고문헌
# https://www.daleseo.com/python-typing/