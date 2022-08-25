from typing import Dict, List, Tuple
from typing import Sequence, TypeVar, Any
from typing import Union

def typing_basic():
    typing_list: List[str] = ["a1", "b1", "c1"]
    typing_tuple : Tuple[int, int] = (10, 20)
    typing_dict : Dict[str, bool] = {'a':True, 'b':False}
    print(typing_list, typing_tuple, typing_dict, )

def typing_basic2(a:float, b:float) -> float:
    typing_a, typing_b = a, b
    return typing_a + typing_b

T = TypeVar('T')
def typing_basic3(val: Sequence[T])->T:
    return val[0]

# Any : 어느것이 와도 괜찮음
def typing_basic4(val: Any)-> Any:
    return val

# Union : Any보다 조금 더 구체적으로 정함
def typing_basic5(val : Union[int,float]):
    return val

if __name__ == "__main__":
    typing_basic()
    print(typing_basic2(3.14, 2.5))
    print(typing_basic3([77,2,3]))
    print(typing_basic4('hh'), type(typing_basic4('hh')))
    print(typing_basic5(3))
    

