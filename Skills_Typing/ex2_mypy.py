# mypy
def add(a: int, b: int) -> int:  # int형 변수 a와 b를 입력받아서 int형 값을 반환
    return a + b

if __name__ == "__main__":
    add(1, 2) # 성공
    add('h', 3) # error 발생
    